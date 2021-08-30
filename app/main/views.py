from app.moderator.forms import RegisterArticle
from app.main.forms import CommentsForm, MailSub
from app.decorators import admin_required
from app.request import get_quotes
from flask import render_template,redirect,url_for,abort,flash,request
from . import main
from ..decorators import  admin_required,permission_required
from flask_login import current_user, login_required
import os

from ..models import Article, Comment, Permission, Subscriber, Users
from .. import db,photos
from .. import db
import requests
#views

@main.route('/',methods=['GET','POST'])
def index():
   mailform=MailSub()
   hello="Welcome to quotes center we have you"
   quotes=get_quotes()
   print(quotes)

   blogposts=Article.query.order_by(Article.time.desc()).all()
   if request.method=='POST':
      email=request.form.get('mail')
      print(email)
      sub=Subscriber(email=email)
      sub.save_subscriber()
      subscribe_user(email=email,user_group_email="newletter@sandboxc9434e3f8bcb41fd8ecdca381c68de98.mailgun.org",api_key='6b3b12dd6292b6c6e2096ea4272416d5-fb87af35-59f2b86e'
)
   print(blogposts)

   return render_template('maintemplates/index.html',hello=quotes,blogposts=blogposts,mailform=mailform)

def subscribe_user(email,user_group_email,api_key):
   resp=requests.post(f'https://api.mailgun.net/v3/lists/{user_group_email}/members')
   auth=('api',api_key),
   data={'subscribed':
   True,
   'address':email}
   print(resp)
   return resp
@main.route('/profile')
def profile():
    return render_template('authtemplates/profile.html')

@main.route('/viewPost/<int:id>',methods=['Post','GET'])
def viewpost(id):
    form=CommentsForm()
    article=Article.query.filter_by(id=id).first()
    blogposts=Article.query.order_by(Article.time.desc()).all()
    post=Article.query.filter_by(id=id).first()
    commentor=current_user._get_current_object()
    if form.validate_on_submit():
       comment=Comment(comments=form.comment.data,article=post,commentor=commentor)
       db.session.add(comment)
       db.session.commit()
       return redirect(url_for('main.viewpost',id=id))
    return render_template('maintemplates/comments.html',post=post,blogposts=blogposts,form=form)
@main.route('/viewFull/<int:id>',methods=['Post','GET'])
def viewFull(id):
   article=Article.query.filter_by(id=id).first()
   return render_template('maintemplates/fullpost.html',article=article)



@main.route('/admin')
@login_required
@admin_required
def from_admins_only():
   return 'for Admins only'

@main.route('/delete_comment/<int:id>')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def del_comment(id):
   com_to_del=Comment.query.filter_by(id=id).first()
   db.session.delete(com_to_del)
   comments=Comment.query.all()
   db.session.commit()
   return redirect(url_for('main.moderate_comments'))
   


@main.route('/write_articles',methods=['POST','GET'])
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def moderate_comments():
   comments=Comment.query.all()
   return render_template('maintemplates/moderate_comments.html',comments=comments)

@main.route('/approve_comment',methods=['POST','GET'])
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def apprv_comment():
    flash('comment approved')
    return redirect(url_for('main.moderate_comments'))

@main.route('/moderate_posts',methods=['POST','GET'])
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def moderate_posts():
   form=RegisterArticle()
   posts=Article.query.filter_by(user_id=current_user.id).all()
   print(posts)
   return render_template('maintemplates/moderate_posts.html',posts=posts,form=form)

@main.route('/delete_post/<int:id>',methods=['POST','GET'])
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def del_posts(id):
   form=RegisterArticle()
   com_to_del=Article.query.filter_by(id=id).first()
   db.session.delete(com_to_del)
   posts=Article.query.all()
   db.session.commit()
   return redirect(url_for('main.moderate_posts'))

@main.route('/edit_post/<int:id>',methods=['POST','GET'])
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def edit_posts(id):
   form=RegisterArticle()
   art=Article.query.filter_by(id=id).first()
   print(art)
   if art is None:
      abort(404)
   if form.validate_on_submit():
 
      art.article_body=form.article_body.data
      art.title=form.title.data
      print(art)
      db.session.add(art)
      db.session.commit()
      return redirect(url_for('main.moderate_posts'))
   
      
   return render_template('maintemplates/update_post.html',form=form)
  


from flask_login.utils import login_required
from app.models import Article, Users
from . import moderator
from .forms import  RegisterArticle
from .. import db
from flask import redirect,url_for,render_template
from flask_login import current_user
from ..models import Permission, Subscriber
from ..email import  send_email, send_post_email
@moderator.route('/add_articles',methods=['POST','GET'])
@login_required
def add_article():
  
    form=RegisterArticle()
   
    # user=Users.query.filter_by(email=form.email.data).first()
    
    #     return redirect(url_for('auth.signup'))
    
    
    # new_user=Users(email=email,name=name,form=form)
    # return redirect(url_for('auth.login'))
    

    if current_user.can(Permission.WRITE_ARTICLES) and form.validate_on_submit():
        user=current_user._get_current_object()
        post=Article(article_body=form.article_body.data,author=user,title=form.title.data,video=form.video.data)
        db.session.add(post)
        db.session.commit()
        

        subscribers=Subscriber.query.all()
        for subscriber in subscribers:

            send_post_email('New Post','authtemplates/email/confirmer',post=post,to=subscriber.email)
            print(subscriber)    
        return redirect(url_for('main.index'))
    return render_template('moderatortemplates/add.html',form=form)

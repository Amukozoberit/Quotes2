from app.email import send_email
from flask.helpers import flash
from flask_login import login_user
from flask_login.utils import login_required, logout_user
from app.auth.forms import Login, Register
from ..models import Users
from flask import Blueprint
from flask import url_for,redirect,request,Flask
from flask import render_template
from .. import db


from . import auth


@auth.route('/login',methods=['POST','GET'])
def login():
    form=Login()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        print(user)
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
    
        flash('logged in sucesfuly')
        redirect(url_for('main.index'))
    return render_template('authtemplates/login.html',form=form)



@auth.route('/signup',methods=['POST','GET'])
def signup():
    form=Register()
   
    # user=Users.query.filter_by(email=form.email.data).first()
    
    #     return redirect(url_for('auth.signup'))
    
    
    # new_user=Users(email=email,name=name,form=form)
    # return redirect(url_for('auth.login'))
    if form.validate_on_submit():
        user=Users(email=form.email.data,name=form.name.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        
        send_email(user.email,'Welcoming email','authtemplates/email/confirm',user=user)
        return redirect(url_for('auth.login'))
    return render_template('authtemplates/register.html',form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
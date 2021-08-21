from flask.helpers import flash
from flask_login import login_manager
from app.auth.forms import Login, Register
from ..models import Users
from flask import Blueprint
from flask import url_for,redirect,request,Flask
from flask import render_template


from . import auth


@auth.route('/login',methods=['POST','GET'])
def login():
    form=Login()
    if form.validate_on_submit():
        user=None
        login_user(user)
        flash('leoged in sucesfuly')
    return render_template('authtemplates/login.html',form=form)



@auth.route('/signup',methods=['POST','GET'])
def signup():
    form=Register()
    # email=request.form.get('email')
    # name=request.form.get('name')
    # password=request.form.get('password')
    # user=Users.query.filter_by(email=email).first()
    # if user:
    #     return redirect(url_for('auth.signup'))
    
    
    # new_user=Users(email=email,name=name,form=form)
    # return redirect(url_for('auth.login'))
    return render_template('authtemplates/register.html',form=form)



@auth.route('/logout')
def logout():
    return 'Logout'
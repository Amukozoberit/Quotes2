from app.models import Users
from flask_login import login_manager
from flask_login.utils import confirm_login
from flask_wtf import Form
from wtforms import StringField,IntegerField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import Email, Required



class Register(Form):
    name=StringField('name',validators=[Required()])
    email=StringField('Email',validators=[Required(),Email()])
    password=PasswordField('Password',validators=[Required()])
    confirm_password=PasswordField('Password',validators=[Required()])
    submit=SubmitField('submit')

class Login(Form):
    email=StringField('Email',validators=[Required(),Email()])
    password=PasswordField('Password',validators=[Required()])
    submit=SubmitField('submit')
    
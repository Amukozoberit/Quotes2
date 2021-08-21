from wtforms.fields.core import BooleanField
from app.models import Users
from flask_login import login_manager
from flask_login.utils import confirm_login
from flask_wtf import Form
from wtforms import StringField,IntegerField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import Email, EqualTo, Required, ValidationError



class Register(Form):
    name=StringField('name',validators=[Required()])
    email=StringField('Email',validators=[Required(),Email()])
    password=PasswordField('Password',validators=[Required(),EqualTo('confirm_password',message='Passwords must match')])
    confirm_password=PasswordField('Confirm Password',validators=[Required()])
    submit=SubmitField('submit')


    def validate_email(self,data_field):
        if Users.query.filter_by(email=data_field.data).first():
            raise ValidationError('Theres a user with that email')
    def validate_name(self,data_field):
        if Users.query.filter_by(name=data_field.data).first():
            raise ValidationError('Theres a user with that Username')



class Login(Form):
    email=StringField('Email',validators=[Required(),Email()])
    password=PasswordField('Password',validators=[Required()])
    remember=BooleanField('Remember me')
    submit=SubmitField('submit')
  
    


    def validate_email(self,data_field):
        if not Users.query.filter_by(email=data_field.data).first():
            raise ValidationError('Theres no user with that email')
    
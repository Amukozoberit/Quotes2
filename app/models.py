from flask_login import UserMixin
from sqlalchemy.orm import backref
from . import db
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(100),unique=True)
    password_secure=db.Column(db.String(100))
    name=db.Column(db.String(1000))
    roles_id=db.Column(db.Integer,db.ForeignKey('roles.id'))

    @property
    def password(self):
        '''password ensures password is write only not read'''
        raise AttributeError('password is not readbale atribute')

    @password.setter
    def password(self,password):
        '''after pass set calls generatepass that writes the hashed pasword to password_hash field pass cant be recovered once hashed'''
        self.password_secure=generate_password_hash(password)


    def verify_password(self,password):
        '''checks if password hashed === with password'''
        return check_password_hash(self.password_secure,password)

    def __repr__(self):
        return f'Users {self.name}'



class Roles(db.Model):
    __tablename__='roles'    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64))
    users=db.relationship('Users',backref="user_role",lazy="dynamic")  
# class quote():
#    def __init__(self,author,id,quote,permalink)
#    self.author=author
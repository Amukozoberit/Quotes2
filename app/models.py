from flask_login import UserMixin
from flask_login.mixins import AnonymousUserMixin
from flask_principal import Permission
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
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
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
  
   
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

    def __init__(self,**kwargs):
            super(Users,self).__init__(**kwargs)
            if self.role is None:
                # if self.email==current_app.config['FLASKY_ADMIN']:
                if self.email=='mwasheberit@gmail.com':
                    self.role=Roles.query.filter_by(permissions=0x0ff).first()
                if self.email=='mwasheb@gmail.com':
                    self.role=Roles.query.filter_by(permissions=0x0f).first()
                if self.role is None:
                    self.role=Roles.query.filter_by(default=True).first()



   
    def can(self,permissions):
            return self.role is not None and  (self.role.permissions & permissions)==permissions
    def is_administrator(self):
            return self.can(Permission.ADMINISTER)
    def __repr__(self):
        return f'Users {self.name}'



class Roles(db.Model):
    __tablename__='roles'    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64))
    default=db.Column(db.Boolean,default=False,index=True)
    permissions=db.Column(db.Integer)
    users=db.relationship('Users',backref='role',lazy='dynamic')


    @staticmethod
    def insert_roles():
        roles = {
        'User': (Permission.FOLLOW |
        Permission.COMMENT ,
         True),
        'Moderator': (Permission.FOLLOW |
        Permission.COMMENT |
        Permission.WRITE_ARTICLES |
        Permission.MODERATE_COMMENTS, False),
        'Administrator': (0xff, False)
        }
        for r in roles:
            role = Roles.query.filter_by(name=r).first()
            if role is None:
                role = Roles(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
            db.session.commit()



     
       
class AnonymousUser(AnonymousUserMixin):
    def can(self,permissions):
        return False

    def is_administrator(self):
        return False
login_manager.anonymous_user = AnonymousUser
class Permission:
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_ARTICLES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTER = 0x80

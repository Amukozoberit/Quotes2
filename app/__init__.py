from logging import Manager
from flask import Flask
from flask_security.core import Security
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate,MigrateCommand
from flask_mail import Mail
import requests
from flask_uploads import UploadSet,configure_uploads,IMAGES
bootstrap=Bootstrap()
db=SQLAlchemy(session_options={"autoflush": False})
login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'
security=Security()
mail = Mail()
photos=UploadSet('photos',IMAGES)

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config_options[config_name])
   
    bootstrap.init_app(app)
    mail.init_app(app)
    configure_uploads(app,photos)


    #register blueprint
    from . main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    from . auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    from . posts import posts as posts_blueprint
    app.register_blueprint(posts_blueprint,url_prefix='/blogposts')

    from . moderator import moderator as moderator_blueprint
    app.register_blueprint(moderator_blueprint,url_prefix='/moderate')

    db.init_app(app)
    login_manager.init_app(app)


    
  


    from .request import configure_request
    configure_request(app)
   
    # from .request import configure_request
    # configure_request(app)
    return app
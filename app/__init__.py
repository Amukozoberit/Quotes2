from logging import Manager
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import  SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate,MigrateCommand

bootstrap=Bootstrap()
db=SQLAlchemy()
login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config_options[config_name])
   
    bootstrap.init_app(app)


    #register blueprint
    from . main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    from . auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    
    db.init_app(app)
    login_manager.init_app(app)
  
   
    # from .request import configure_request
    # configure_request(app)
    return app
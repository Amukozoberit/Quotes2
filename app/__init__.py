from flask import Flask
from config import config
from flask_bootstrap import Bootstrap

bootstrap=Bootstrap()

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init(app)
    bootstrap.init_app(app)


    #register blueprint
    from . main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    from . auth import main as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')


    from .request import configure_request
    configure_request(app)
    return app
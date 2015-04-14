# ----------------------------------------------------
# APPLICATION FACTORY CREATES THE APPLICATION INSTANCE
# ----------------------------------------------------
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy

# import relevant flask-login class
from flask.ext.login import LoginManager
from config import config

# instantiate and configure flask-login LoginManager
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
# configure a route to a view function
login_manager.login_view = 'auth.login'


def create_app(config_name):
    """ create_app : dict[key] -> app 
    a factory function to initialize extensions and register
    blueprints with the app instance. call it in your launch
    script. """

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # register flask-login with the app, define callback in the model
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # register auth blueprint 
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # return the initialized app
    return app




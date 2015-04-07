# APPLICATION FACTORY CREATES THE APPLICATION INSTANCE

# imports
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

# uninitialized constructors
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

# application factory function
def create_app(config_name):
    """ create_app : dict[key] -> app """

    # initialize and configure the app
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # initialize extensions with the app
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # attach routes and error pages from blueprint here
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # return the initialized app
    return app




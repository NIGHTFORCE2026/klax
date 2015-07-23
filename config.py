# ----------------------------------------------------
# CONFIGURATION OPTIONS FOR THE APP AND ITS EXTENSIONS
# ----------------------------------------------------
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# common settings 
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'shesanuptownmodel'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = 'smtp.googlemail.com' 
    MAIL_PORT = 587 
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    KLAX_MAIL_SUBJECT_PREFIX = '[KLAX]'
    KLAX_MAIL_SENDER = 'KLAX Admin <klax@example.com>'
    KLAX_ADMIN = os.environ.get('KLAX_ADMIN')
    KLAX_POSTS_PER_PAGE = 20

    # configuration-specific initialization method
    @staticmethod
    def init_app(app):
        pass

# settings for different development databases
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


# collect config classes into dictionary to use as parameters elsewhere
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}

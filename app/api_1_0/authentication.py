from flask import g
from ..models import User, AnonymousUser
from flask.ext.httpauth import HTTPBasicAuth
from .errors import unauthorized
# link this to the api blueprint
from . import api

# initialize the extension in the api blueprint package, not app package
auth = HTTPBasicAuth()

# decorated callback functions are the interface to flask-httpauth 
@auth.verify_password
def verify_password(email, password):
    """ verify a user's password, 
    assign a user to global context to be accessed by the rest of the system,
    return True on success """
    if email = '':
        # anons are identified by blank email
        g.current_user = AnonymousUser()
        return True
    user = User.query.filter_by(email=email).first()
    if not user:
        # bogus users aren't allowed
        return False
    g.current_user = user
    return user.verify_password(password)

@auth.errorhandler
def auth_error():
    """ callback using error handler in errors.py """
    return unauthorized('Invalid credentials')

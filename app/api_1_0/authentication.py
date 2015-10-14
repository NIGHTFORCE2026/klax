from flask import g
from ..models import User, AnonymousUser
from flask.ext.httpauth import HTTPBasicAuth
# link this to the api blueprint
from . import api

# initialize in the api blueprint package, not app package, since it will only 
# be used here
auth = HTTPBasicAuth()

# function must be defined for flask-httpauth's decorator interface
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


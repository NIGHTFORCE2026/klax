from flask import g, jsonify
from flask.ext.httpauth import HTTPBasicAuth
from ..models import User, AnonymousUser
from .errors import unauthorized, forbidden
# link this to the api blueprint
from . import api

# initialize the extension in the api blueprint package, not app package
auth = HTTPBasicAuth()

# decorated callback functions are the interface to flask-httpauth 
@auth.verify_password
def verify_password(email_or_token, password):
    """ verify a user's password, 
    assign a user to global context to be accessed by the rest of the system,
    set token_used so view functions can distinguish bw authentication types,
    return True on success """
    if email_or_token == '':
        # blank email identify anons 
        g.current_user = AnonymousUser()
        return True
    if password == '':
        # blank password identify a token, so verify it 
        g.current_user = User.verify_auth_token(email_or_token)
        g.token_used = True
        return g.current_user is not None
    user = User.query.filter_by(email=email_or_token).first()
    if not user:
        # bogus users aren't allowed
        return False
    g.current_user = user
    g.token_used = False
    return user.verify_password(password)

@auth.error_handler
def auth_error():
    """ callback using error handler in errors.py """
    return unauthorized('Invalid credentials')

@api.before_request
@auth.login_required
def before_request():
    """ all routes in the api blueprint need to be protected, so set the
    login_required decorator on a request hook """
    if not g.current_user.is_anonymous and \
            not g.current_user.confirmed:
        return forbidden('Unconfirmed account')

# before_request hooks apply to this route
@api.route('/token')
def get_token():
    """ send authentication token to a client """
    if g.current_user.is_anonymous() or g.token_used:
    # token_used prevents clients with old tokens from
    # requesting a new one
        return unauthorized('Invalid credentials')
    return jsonify({'token': g.current_user.generate_auth_token(
        expiration=3600), 'expiration': 3600})


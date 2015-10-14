# import blueprint
from flask import Blueprint
# initialize it
api = Blueprint('api', __name__)
# import auth, resource handlers, error handlers
from . import authentication, posts, users, comments, errors


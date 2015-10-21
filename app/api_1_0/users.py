from flask import jsonify, request, current_app, url_for
from . import api
from ..models import User, Post

@api.route('/users/<int:id>')
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_json())

@api.route('/users/<int:id>/posts/')
def get_user_posts():
    pass

@api.route('/users/<int:id>/timeline/')
def get_user_followed_posts():
    pass

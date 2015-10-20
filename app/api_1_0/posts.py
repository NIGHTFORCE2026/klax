from flask import jsonify, request, g, abort, url_for, current_app
from .. import db
from ..models import Post, Permission
from . import api
from .errors import forbidden

@api.route('/posts/<int:id>')
def get_post(id):
    """ return a single post as json """
    post = Post.query.get_or_404(id)
    return jsonify(post.to_json())

@api.route('/posts')
def get_posts():
    """ return a collection of posts as json """
    posts = Post.query.all()
    return jsonify({'posts': [post.to_json() for post in posts] })


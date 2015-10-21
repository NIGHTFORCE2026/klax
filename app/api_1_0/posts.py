from flask import jsonify, request, g, abort, url_for, current_app
from .. import db
from ..models import Post, Permission
from . import api
from .errors import forbidden
from .decorators import permission_required

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

@api.route('/posts/', methods=['POST'])
@permission_required(Permission.WRITE_ARTICLES)
def new_post():
    """ create a new post object from json in client request
    and return a json response containing the post """
    post = Post.from_json(request.json)
    post.author = g.current_user
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_json()), 201, \
    { 'Location': url_for('api.get_post', id=post.id, _external=True) }


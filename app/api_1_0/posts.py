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
    """ return a paginated collection of posts as json """
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.paginate(
            page, per_page=current_app.config['KLAX_POSTS_PER_PAGE'], 
            error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_posts', page=page-1, _external=True)
    next = None
    if pagination.has_next:
        next = url_for('api.get_posts', page=page+1, _external=True)
    return jsonify({
        'posts': [post.to_json() for post in posts],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })

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

@api.route('/posts/<int:id>', methods=['PUT'])
@permission_required(Permission.WRITE_ARTICLES)
def edit_post(id):
    """ edit a post object attribute from json in client request
    and return a json response containing the post """
    post = Post.query.get_or_404(id)
    if g.current_user != post.author and \
            not g.current_user.can(Permission.ADMINISTER):
        return forbidden('Insufficient permissions')
    post.body = request.json.get('body', post.body)
    db.session.add(post)
    return jsonify(post.to_json())


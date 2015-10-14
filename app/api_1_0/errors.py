from flask import jsonify
from . import api

def bad_request():
    response = jsonify({'error': 'bad request'})
    response.status_code = 400
    return response

def unauthorized():
    response = jsonify({'error': 'unauthorized'})
    response.status_code = 401
    return response

def forbidden():
    response = jsonify({'error': 'forbidden'})
    response.status_code = 403
    return response

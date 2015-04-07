# register the blueprint
from flask import render_template
from . import main

# use app_errorhandler() to use application-wide error handlers
@main.app_errorhandler(404)
def request_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

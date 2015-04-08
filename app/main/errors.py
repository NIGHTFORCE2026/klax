# register 'main' package's blueprint 
from flask import render_template
from . import main

# register routes with 'main' package's blueprint 
# app_errorhandler() registers application-wide error handlers
@main.app_errorhandler(404)
def request_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

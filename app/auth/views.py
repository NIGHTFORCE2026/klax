from flask import render_template
# import the blueprint 
from . import auth

# define a route relative to the blueprint
@auth.route('/login')
def login():
    # looks in app/templates/auth/login.html
    return render_template('auth/login.html')

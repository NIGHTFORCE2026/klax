from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from . import auth
from ..models import User
from .forms import LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # serve form to a GET request 
    form = LoginForm()
    # process form data from POST request
    if form.validate_on_submit():
        # search db email for form email
        user = User.query.filter_by(email=form.email.data).first()
        # verify password in form password
        if user is not None and user.verify_password(form.password.data):
            # log in user, send em to the next page or the main.index endpoint
            login_user(user, form.remember_me.data)
            return redirect(request.args,get('next') or url_for('main.index'))
        # else, give them an error message
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
# protect the route
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

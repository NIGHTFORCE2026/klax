# [x] initial application
# [x] added dynamic route
# [x] integrated templates
# [x] integrated an extension: flask-script 
# [x] bootstrap-template integration: user.html
# [x] template: generalized an app template for inheritance
# [x] templates: error pages
# [x] dynamic URLs, static files using favicons
# [x] integrated flask-moment: JS time library
# [x] web forms with flask-wtf (4a)
#       imports
#       configure an encryption key
#       form classes
#       html rendering of forms
#       form handling in view functions
# [x] redirects and user sessions (4b)
# [x] message flashing (4c)
# [ ] Database models with Flask-SQLAlchemy (5a)

import os
from flask import Flask, render_template, url_for, session, redirect, flash
from datetime import datetime
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required 

# import the extension
from flask.ext.sqlalchemy import SQLAlchemy

# define a directory reference where the db should reside
basedir = os.path.abspath(os.path.dirname(__file__))

# set configuration parameters for the db location and auto commits
app = Flask(__name__)
app.config['SECRET_KEY'] = 'shesanuptownmodel'
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# integrate the extension
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)

# define the db schema represented in UML
#   associate tables to classes 
#   associate columns to attributes
#   configure primary keys
#   associate tables via foreign key
#   associate objects 
#   configure column types
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username




class NameForm(Form):
    name = StringField('What is your name?', validators = [Required()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def request_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods = ['GET', 'POST'])
def index():
    a_form = NameForm()
    # flash a message if name in session different from name in input
    if a_form.validate_on_submit():
        prior_name = session.get('name')
        if prior_name is not None and prior_name != a_form.name.data:
            flash('Looks like you have changed your name!')
        session['name']= a_form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form = a_form, name = session.get('name'))


if __name__ == '__main__':
    manager.run()


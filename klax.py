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
# [x] Database models with Flask-SQLAlchemy (5a)
# [x] Database use in the application (5b)
# [x] Shell context (5c)
# [x] Database migrations with Flask-Migrate (5d)
# [x] Email support with Flask-Mail (6a)
# [x] Asynchronous emails (6b)


# import threading library
import os
from threading import Thread
from flask import Flask, render_template, url_for, session, redirect, flash
from datetime import datetime
from flask.ext.script import Manager, Shell
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required 
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.mail import Mail, Message

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'shesanuptownmodel'
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['MAIL_SERVER'] = 'smtp.googlemail.com' 
app.config['MAIL_PORT'] = 587 
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['KLAX_MAIL_SUBJECT_PREFIX'] = '[KLAX]'
app.config['KLAX_MAIL_SENDER'] = 'KLAX Admin <klax@example.com>'
app.config['KLAX_ADMIN'] = os.environ.get('KLAX_ADMIN')

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

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

# create an application context for mail.send()
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

# embed threaded mail.send() in a thread
def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['KLAX_MAIL_SUBJECT_PREFIX'] + ' ' + subject, 
            sender=app.config['KLAX_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    # create the thread
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr

class NameForm(Form):
    name = StringField('What is your name?', validators = [Required()])
    submit = SubmitField('Submit')

def make_shell_context():
    return dict(app=app, db=db, Role=Role, User=User)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@app.errorhandler(404)
def request_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods = ['GET', 'POST'])
def index():
    a_form = NameForm()
    if a_form.validate_on_submit():
        user = User.query.filter_by(username=a_form.name.data).first()
        if user is None:
            user = User(username=a_form.name.data)
            db.session.add(user)
            session['known'] = False
            if app.config['KLAX_ADMIN']:
                send_email(app.config['KLAX_ADMIN'], 'New User', 
                        'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name']= a_form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=a_form, name=session.get('name'), 
            known=session.get('known', False)) 

if __name__ == '__main__':
    manager.run()


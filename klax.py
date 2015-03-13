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
# [ ] message flashing (4c)


# import session request object, redirect
from flask import Flask, render_template, url_for, session, redirect
from datetime import datetime
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'shesanuptownmodel'


manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

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
    name = None
    a_form = NameForm()
    if a_form.validate_on_submit():
        # store input in user session, redirect
        session['name']= a_form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form = a_form, name = session.get('name'))


if __name__ == '__main__':
    manager.run()


from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import User
from ..email import send_email
# register the blueprint
from . import main
from .forms import NameForm

# route decorator comes from Blueprint called main
@main.route('/', methods = ['GET', 'POST'])
def index():
    a_form = NameForm()
    if a_form.validate_on_submit():
        user = User.query.filter_by(username=a_form.name.data).first()
        if user is None:
            user = User(username=a_form.name.data)
            db.session.add(user)
            session['known'] = False
            if current_app.config['KLAX_ADMIN']:
                send_email(current_app.config['KLAX_ADMIN'], 'New User', 
                        'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name']= a_form.name.data
        # register endpoint to main.index; uses the short notation
        return redirect(url_for('.index'))
    return render_template('index.html', form=a_form, name=session.get('name'), 
            known=session.get('known', False)) 

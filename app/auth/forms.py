from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email

class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), 
                                            Email()])
    password = PasswordField('Password', validators=[Required()])
    # True sets cookie to restore user session if they close browser
    # False user session expires when browser closed
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
    


#-------------------------------------------
# SENDS EMAIL ALERTS
#-------------------------------------------
from threading import Thread
from flask import current_app, render_template
from flask.ext.mail import Message
from . import mail

# create an application context for mail.send()
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

# embed threaded mail.send() in a thread
def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(current_app.config['KLAX_MAIL_SUBJECT_PREFIX'] + ' ' + subject, 
            sender=current_app.config['KLAX_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    # create the thread
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr

# [x] initial application
# [x] added dynamic route
# [x] integrated templates
# [x] integrated an extension: flask-script 
# [x] bootstrap-template integration: user.html
# [x] template: generalized an app template for inheritance
# [x] templates: error pages
# [x] dynamic URLs, static files using favicons
# [ ] integrated flask-moment: JS time library
# [ ] web forms with flask-wtf (4a)
# [ ] redirects and user sessions (4b)
# [ ] message flashing (4c)


# import datetime library to generate timestamp; import Flask-Moment
from flask import Flask, render_template, url_for
from datetime import datetime
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.errorhandler(404)
def request_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# generate and return a timestamp to the template
@app.route('/')
def index():
    return render_template('index.html', 
            a_timestamp = datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)


if __name__ == '__main__':
    manager.run()


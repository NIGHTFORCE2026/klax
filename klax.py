# [x] initial application
# [x] added dynamic route
# [x] integrated templates
# [x] integrated an extension: flask-script 
# [x] bootstrap-template integration: user.html
# [x] template: generalized an app template for inheritance
# [ ] templates: error pages
# [ ] dynamic URLs, static files
# [ ] integrated flask-moment: JS time library
# [ ] web forms with flask-wtf (4a)
# [ ] redirects and user sessions (4b)
# [ ] message flashing (4c)


from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.errorhandler(404)
def request_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)


if __name__ == '__main__':
    manager.run()


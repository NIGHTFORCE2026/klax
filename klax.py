# [x] initial application
# [x] added dynamic route
# [x] integrated templates
# [x] integrated an extension: flask-script 
# [ ] bootstrap-template integration: user.html
# [ ] template: generalized an app template for inheritance
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)


if __name__ == '__main__':
    manager.run()


# [x] initial application
# [ ] added dynamic route
# [ ] integrated templates
# [ ] integrated templates 2
# [ ] bootstrap-template integration: user.html
# [ ] template: generalized an app template for inheritance
# [ ] templates: error pages
# [ ] dynamic URLs, static files
# [ ] integrated flask-moment: JS time library
# [ ] web forms with flask-wtf (4a)
# [ ] redirects and user sessions (4b)
# [ ] message flashing (4c)


from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    app.run(debug = True)


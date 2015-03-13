# [x] initial application
# [x] added dynamic route
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


from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)


if __name__ == '__main__':
    app.run(debug = True)


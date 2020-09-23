from flask import Flask

appJX = Flask(__name__)

@appJX.route('/')
def index():
 return '<h1>Hello World!</h1>'

@appJX.route('/user/<name>')
def user(name):
 return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
 appJX.run(debug=True)

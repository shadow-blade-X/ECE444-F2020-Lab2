from flask import Flask

appJX = Flask(__name__)

@appJX.route('/')

def index():
 return '<h1>Hello World!</h1>'

if __name__ == '__main__':
 appJX.run(debug=True)

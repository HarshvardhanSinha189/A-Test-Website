from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello You are here! about page <a href="/about"> about </a> '

@app.route('/about')
def hello_world():
    return 'Welcome to the about page '

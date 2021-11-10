from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return 'index page'

@app.route('/hi')
def hi():
    return 'hi guys!'
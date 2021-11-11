from flask import Flask

app = Flask(__name__)

@app.route('/projects/')
def projects():
    return 'the project page'
    
@app.route('/about')
def about():
    return 'the about page'
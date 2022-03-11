from unicodedata import name
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route('/signin')
def signin():
    return "signin"

@app.route('/signup')
def signup():
    return "signnup"

if __name__== "__main__":
    app.run(debug=True)
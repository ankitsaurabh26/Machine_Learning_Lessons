# WSGI(Web Server Gateway Interface) protocol & Jinja2 Template Engine

from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome buddy !!"

@app.route('/members')
def members():
    return "Welcome to the membership !!"

if __name__ == '__main__':
    app.run(debug=True) # debug = True : will automatically restart the application whenever we apply some changes
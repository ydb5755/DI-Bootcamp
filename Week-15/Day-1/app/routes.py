from app import flask_app
from flask import render_template

@flask_app.route('/<username>')
def home(username):
    return render_template('index.html', username=username)
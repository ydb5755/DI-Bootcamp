import flask

app = flask.Flask(__name__)

@app.rout('/')
def index():
    return 'Hello'

@app.rout('/<username>')
def index1(username):
    return f'Hello {username}'
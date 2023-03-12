import flask

app = flask.Flask(__name__)

@app.rout('/')
def index():
    return 'Hello'
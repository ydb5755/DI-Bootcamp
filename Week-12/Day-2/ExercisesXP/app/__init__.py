import flask
from config import Config


app = flask.Flask(__name__)
app.config.from_object(Config)

from app import routes
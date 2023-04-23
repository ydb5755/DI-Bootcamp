from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


db = SQLAlchemy()
migrate = Migrate()


# def create_app():
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app,db)

    # return app

from app import routes

def crypto_data_call():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
    parameters = {
    'start':'1',
    'limit':'20'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data['data']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e
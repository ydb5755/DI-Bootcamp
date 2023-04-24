from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from flask import Flask, redirect, url_for
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    # login_manager.login_view 
    @app.route('/')
    def _():
        return redirect(url_for('profiles.home'))
    from app.profiles import profiles
    app.register_blueprint(profiles)

    return app







def swapi_data_call(cat, num, attr):
    url = 'https://swapi.dev/api/'

    session = Session()
    try:
        response = session.get(url + f'{cat}/{num}/')
        data = json.loads(response.text)
        return data[attr]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e
    


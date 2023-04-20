import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'portfolio.db')
app.config['SECRET_KEY'] = '123456'

db = SQLAlchemy(app)
migrate = Migrate(app,db)

from app.accounts import accounts_bp
from app.films import films_bp

app.register_blueprint(accounts_bp, url_prefix="/accounts")
app.register_blueprint(films_bp, url_prefix="/films")


from app.models import Category
def populate_categories():
    with app.app_context():
        action          = Category(name='Action')
        comedy          = Category(name='Comedy')
        science_fiction = Category(name='Science-Fiction')
        drama           = Category(name='Drama')
        horror          = Category(name='Horror')
        action.save_category()
        comedy.save_category()
        science_fiction.save_category()
        drama.save_category()
        horror.save_category()

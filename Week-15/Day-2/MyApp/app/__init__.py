import os
from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'portfolio.db')
    app.config['SECRET_KEY'] = '123456'

    db.init_app(app)
    migrate.init_app(app,db)
    login_manager = LoginManager(app)

    # login_manager.init_app(app)
    login_manager.login_view = "accounts.login"  # type: ignore
    # @login_manager.login_view
    # def login():
    #     # Render the login template.
    #     return render_template('login.html')
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from app.accounts import accounts_bp
    from app.films import films_bp

    app.register_blueprint(accounts_bp, url_prefix="/accounts")
    app.register_blueprint(films_bp, url_prefix="/films")
    return app

from app.models import Category
def populate_categories():
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
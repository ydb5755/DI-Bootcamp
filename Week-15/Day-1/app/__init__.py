from flask import Flask

flask_app = Flask(__name__)

from app.filters import add_gmail_to_name

flask_app.jinja_env.filters['add_5'] = add_gmail_to_name

from app import routes

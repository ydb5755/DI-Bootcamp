from flask import Blueprint

accounts_bp = Blueprint('accounts_bp', __name__, template_folder='views', static_folder='static')


from app.accounts import routes
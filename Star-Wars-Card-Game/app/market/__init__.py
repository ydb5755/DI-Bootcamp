from flask import Blueprint


market = Blueprint('market', __name__, template_folder='templates', static_folder='static', url_prefix='/market')

from app.market import routes
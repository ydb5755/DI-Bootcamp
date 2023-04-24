from flask import Blueprint


profiles = Blueprint('profiles', __name__, template_folder='templates', static_folder='static', url_prefix='/profiles')

from app.profiles import routes
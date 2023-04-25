from flask import Blueprint


forum = Blueprint('forum', __name__, template_folder='templates', static_folder='static', url_prefix='/forum')

from app.forum import routes
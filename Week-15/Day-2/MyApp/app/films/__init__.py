from flask import Blueprint

films_bp = Blueprint('films_bp', __name__, template_folder='views', static_folder='static')


from app.films import routes
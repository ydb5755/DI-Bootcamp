from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(db.Model, UserMixin):
    id       = db.Column(db.Integer, primary_key=True)
    name     = db.Column(db.String(64), unique=True, nullable=False)
    street   = db.Column(db.String(64), nullable=False)
    city     = db.Column(db.String(64), unique=True, nullable=False)
    zipcode  = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f'User (id-{self.id}, name-{self.name}, street-{self.street}, city-{self.city}, zipcode-{self.zipcode})'
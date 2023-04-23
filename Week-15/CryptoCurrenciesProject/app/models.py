from app import db
from flask_login import UserMixin

user_crypto = db.Table('user_crypto',
                       db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                       db.Column('crypto_id', db.Integer, db.ForeignKey('crypto.id'))
)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    crypto_coins = db.relationship('Crypto', secondary=user_crypto, backref='users')


class Crypto(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(64))
    symbol = db.Column(db.String(64))
    slug = db.Column(db.String(64))
    first_historical_data = db.Column(db.String(64))
    last_historical_data = db.Column(db.String(64))
    is_active = db.Column(db.Integer)

    def get_info(self):
        pass



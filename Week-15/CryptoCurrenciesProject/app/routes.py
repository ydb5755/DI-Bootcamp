from flask import current_app, render_template
from app.models import Crypto
from app import app


@app.route('/')
@app.route('/index')
def index():
    all_coins = Crypto.query.all()
    return render_template('index.html', all_coins=all_coins)

@app.route('/details/<coin_id>')
def details(coin_id):
    coin = Crypto.query.filter_by(id=coin_id).first()
    return render_template('specifics.html', coin=coin)
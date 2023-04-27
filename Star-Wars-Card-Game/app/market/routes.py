from app.market import market
from flask_login import login_required, current_user
from flask import render_template, redirect, url_for, flash
from app.profiles.models import Card



@market.route('/marketplace_home')
@login_required
def marketplace_home():
    all_cards = Card.query.all()
    cards_on_market = Card.query.filter_by(on_market=True)
    return render_template('market_home.html',
                           all_cards=all_cards,
                           cards_on_market=cards_on_market)

@market.route('/card/<card_id>')
@login_required
def card_page(card_id):
    card = Card.query.filter_by(id=card_id).first()
    return render_template('card_page.html',
                           card=card)

@market.route('/card/<card_id>/purchase')
@login_required
def purchase(card_id):
    card = Card.query.filter_by(id=card_id).first()
    card_owner = card.current_owner
    card_owner.coins += card.set_price
    current_user.coins -= card.set_price # type: ignore
    card_owner = current_user
    flash('Sale Complete!')
    return redirect(url_for('market.marketplace_home'))

@market.route('/card/<card1_id>/trade')
@login_required
def trade(card1_id, card2_id):
    card1 = Card.query.filter_by(id=card1_id).first()
    card2 = Card.query.filter_by(id=card2_id).first()
    return redirect(url_for('market.marketplace_home'))

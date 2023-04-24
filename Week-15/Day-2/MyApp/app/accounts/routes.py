from flask import render_template, redirect, flash, url_for
from app.accounts import accounts_bp
from app.models import User
from app.accounts.forms import SignUpForm, LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

@accounts_bp.route('/signup', methods=('GET', 'POST'))
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('films_bp.homepage'))
    form = SignUpForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash('This username is already taken, please try another one')
            return redirect(url_for('accounts_bp.signup'))
        if not form.password1.data == form.password2.data:
            flash('Your password doesnt match the confirmation, please try again')
            return redirect(url_for('accounts_bp.signup'))
        pw = generate_password_hash(form.password1.data, method='sha256')
        new_user = User(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    username=form.username.data,
                    password=pw)
        new_user.save_user()
        flash('Youve successfully signed up! Please login to continue')
        return redirect(url_for('accounts_bp.login'))
    return render_template('signup.html', form=form)

@accounts_bp.route('/login', methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('films_bp.homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user or not check_password_hash(user.password, form.password.data):
            flash('Please check your login details and try again.')
            return redirect(url_for('accounts_bp.login'))
        login_user(user, remember=form.remember.data)
        return redirect(url_for('films_bp.homepage'))
    return render_template('login.html', form=form)

@accounts_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('films_bp.homepage'))

@accounts_bp.route('/profile/<user_id>')
@login_required
def profile(user_id):
    user = User.query.filter_by(id=user_id).first()
    return render_template('profile.html', user=user)
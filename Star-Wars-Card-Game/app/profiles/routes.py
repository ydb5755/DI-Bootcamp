from flask import current_app, render_template, redirect, url_for, flash, request
from app.profiles import profiles
from app.profiles.forms import LoginForm, SignUpForm
from flask_login import current_user, login_user, logout_user, login_required
from app.profiles.models import User, Card
from werkzeug.security import generate_password_hash, check_password_hash

@profiles.route('/login', methods=('GET', 'POST'))
def login(): 
    if current_user.is_authenticated: # type: ignore
        return redirect(url_for('forum.forum_home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user or not check_password_hash(user.password, form.password.data):
            flash('Please check your login details and try again.')
            return redirect(url_for('profiles.login'))
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('forum.forum_home'))
        # return redirect(url_for(''))
    return render_template('login.html', form=form)

@profiles.route('/signup', methods=('GET', 'POST'))
def signup(): 
    if current_user.is_authenticated: # type: ignore
        return redirect(url_for('forum.forum_home'))
    form = SignUpForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash('This username is already taken, please try another one')
            return redirect(url_for('profiles.signup'))
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('This email is already taken, please try another one')
            return redirect(url_for('profiles.signup'))
        if not form.password1.data == form.password2.data:
            flash('Your password doesnt match the confirmation, please try again')
            return redirect(url_for('profiles.signup'))
        user = User(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            profile_type = form.profile_type.data,
            username = form.username.data,
            email = form.email.data,
            password = generate_password_hash(form.password1.data, method='sha256')
        )
        user.save_user()
        flash("You've been signed up successfully! Please login to continue")
        return redirect(url_for('profiles.login'))
    return render_template('signup.html', form=form)


@profiles.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('profiles.login'))

@profiles.route('/profile/<user_id>')
@login_required
def profile_page(user_id):
    user = User.query.filter_by(id=user_id).first()
    return render_template('profile_page.html', user=user) 

@profiles.route('/admin')
@login_required
def admin():
    if current_user.is_authenticated and not current_user.id == 1: #type:ignore
        redirect(url_for('forum.forum_home'))
    if not current_user.is_authenticated: #type:ignore
        redirect(url_for('profiles.login'))
    cards_off_market = Card.query.filter_by(on_market=False)
    user = User.query.filter_by(id=1).first()
    return render_template('admin.html',
                           user=user, 
                           cards_off_market=cards_off_market)
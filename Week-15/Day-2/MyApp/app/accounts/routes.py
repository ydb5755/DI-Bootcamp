from flask import render_template
from app.accounts import accounts_bp
from app.models import User
from app.accounts.forms import SignUpForm, LoginForm


@accounts_bp.route('/signup')
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    username=form.username.data,
                    password=form.password1.data)
    return render_template('signup.html')

@accounts_bp.route('/login')
def login():
    return render_template('login.html')

@accounts_bp.route('/logout')
def logout():
    return render_template('logout.html')

@accounts_bp.route('/profile/<user_id>')
def profile(user_id):
    user = User.query.filter_by(id=user_id).first()
    return render_template('profile.html', user=user)
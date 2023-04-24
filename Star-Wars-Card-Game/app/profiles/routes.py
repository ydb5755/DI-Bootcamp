from flask import current_app, render_template, redirect, url_for, flash
from app.profiles import profiles


@profiles.route('/home')
def home():
    return render_template('home.html')


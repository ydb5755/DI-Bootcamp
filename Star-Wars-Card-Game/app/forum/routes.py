from app.forum import forum
from flask import render_template, redirect, url_for, flash
from app.profiles.models import User, Card



@forum.route('/')
def forum_home():
    return render_template('forum_home.html')
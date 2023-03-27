from app import app
from app.models import Book
from app import db
from flask import render_template, flash

@app.route('/')
def home():
    flash('You are at the home page!', 'success')
    flash('Maybe you didnt want to be here...', 'danger')
    return render_template('home.html')

@app.route('/insert/<int:book_id>')
def insert(book_id):
    book = Book(book_id=book_id, title='a', author='b', price=1)
    db.session.add(book)
    db.session.commit()
    return "Hello"
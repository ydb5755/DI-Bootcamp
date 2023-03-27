import flask
from flask import flash, abort

from app import flask_app
from app.models import Book
from app import db


@flask_app.route('/login')
def home_page():
    # some login logic
    flash("username or password are not correct", "error")
    flash("another flashed message", "success")
    return flask.render_template("login.html")


@flask_app.route('/admin')
def admin_page():
    abort(401)
    return flask.render_template("admin.html")

@flask_app.route('/insert/<int:book_id>')
def insert_page(book_id):
    my_book = Book(book_id=book_id, title="my book", author="Bob", price=10)
    db.session.add(my_book)
    db.session.commit()

    return "hello"


def get_all_books():
    return [{"book_id": book.book_id, "title": book.title} for book in Book.query.all()]


@flask_app.shell_context_processor
def make_shell_context():
    return {
        "all_books": get_all_books()
    }

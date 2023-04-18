from flask import render_template, redirect, url_for
from app import app
from app.films import films_bp
from app.films.forms import AddDirectorForm, AddFilmForm
from app.models import Film, Director, Country, Category


@app.route('/')
@films_bp.route("/homepage")
def homepage():
    return render_template("homepage.html")

@films_bp.route('/addFilm')
def addFilm():
    form = AddFilmForm()
    if form.validate_on_submit():
        film = Film(title=form.title.data, 
                    release_date=form.release_date.data,
                    created_in_country=form.created_in_country.data,
                    available_in_countries=form.available_in_countries.data,
                    categories=form.categories.data,
                    director=form.director.data
                    )
        film.save_film()
        country_to_add_to = Country.query.filter_by(name=form.created_in_country.data).first()
        if country_to_add_to:
            country_to_add_to.films.append(film)
        else:
            new_country = Country(name=form.created_in_country.data)
            new_country.save_country()
        director_to_add_to = Director.query.filter_by(name=form.created_in_country.data).first()
        if director_to_add_to:
            director_to_add_to.films.append(film)
        else:
            new_director = Director(first_name=form.director.data)
            new_director.save_director()
        category_to_add_to = Category.query.filter_by(name=form.categories.data).first()
        if category_to_add_to:
            category_to_add_to.films.append(film)
        else:
            new_category = Category(name=form.categories.data)
            new_category.save_category()
        redirect(url_for('films_bp.homepage'))
    return render_template('addFilm.html', form=form)

@films_bp.route('/addDirector')
def addDirector():
    form = AddDirectorForm()
    if form.validate_on_submit():
        director = Director(name=form.name.data)
        director.save_director()
    return render_template('addDirector.html', form=form)
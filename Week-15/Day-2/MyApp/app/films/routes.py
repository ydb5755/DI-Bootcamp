from flask import render_template, redirect, url_for
from app import app, db
from app.films import films_bp
from app.films.forms import AddDirectorForm, AddFilmForm, UpdateDirectorForm
from app.models import Film, Director, Country, Category


@app.route('/')
@films_bp.route("/homepage")
def homepage():
    films = Film.query.all()
    return render_template("homepage.html", films=films)

@films_bp.route('/addFilm', methods=('GET', 'POST'))
def addFilm():
    film_form = AddFilmForm()

    if film_form.validate_on_submit():
        country_to_add_to = Country.query.filter_by(name=film_form.created_in_country.data).first()
        if not country_to_add_to:
            country_to_add_to = Country(name=film_form.created_in_country.data)

        film = Film(title=film_form.title.data, 
                    release_date=film_form.release_date.data,
                    created_in_country=country_to_add_to
                    )
        
        country_to_add_to.films_produced.append(film)
        country_to_add_to.save_country()
        
        for cat in film_form.categories:
            category_to_add_to = Category.query.filter_by(name=cat.data).first()
            film.category.append(category_to_add_to)
            category_to_add_to.films.append(film)

        film.save_film()
        return redirect(url_for('films_bp.homepage'))
    return render_template('addFilm.html', 
                           film_form=film_form
                           )

@films_bp.route('/addDirector', methods=('GET', 'POST'))
def addDirector():
    form = AddDirectorForm()
    all_films = Film.query.all()
    form.film.choices = [f.title for f in all_films]
    if form.validate_on_submit():
        director = Director.query.filter_by(first_name=form.first_name.data, last_name=form.last_name.data).first()
        if director:
            fil = Film.query.filter_by(title=form.film.data).first()
            director.films.append(fil)
            director.save_director()
        else:
            director = Director(first_name=form.first_name.data, last_name=form.last_name.data)
            fil = Film.query.filter_by(title=form.film.data).first()
            director.films.append(fil)
            director.save_director()
        # db.session.commit()
        return redirect(url_for('films_bp.homepage'))
    return render_template('addDirector.html', form=form)


@films_bp.route('/chooseDirector/<film_id>')
def choose_director(film_id):
    directors = Film.query.filter_by(id=film_id).first().director
    return render_template('chooseDirector.html', directors=directors)

@films_bp.route('/editDirector/<director_id>', methods=('GET', 'POST'))
def edit_director(director_id):
    director_to_update = Director.query.filter_by(id=director_id).first()
    form = UpdateDirectorForm()
    if form.validate_on_submit():
        director_to_update.first_name = form.first_name.data
        director_to_update.last_name  = form.last_name.data
        db.session.commit()
        return redirect(url_for('films_bp.homepage'))
    return render_template('editDirector.html', 
                           director_to_update=director_to_update, 
                           form=form)

@films_bp.route('/editFilm/<film_id>', methods=('GET', 'POST'))
def edit_film(film_id):
    film_to_update = Film.query.filter_by(id=film_id).first()
    form = AddFilmForm()
    if form.validate_on_submit():
        film_to_update.title = form.title.data
        film_to_update.release_date = form.release_date.data
        film_to_update.category = []
        if form.categories.data:
            for cat in form.categories.data:
                category_to_add_to = Category.query.filter_by(name=cat).first()
                film_to_update.category.append(category_to_add_to)
                category_to_add_to.films.append(film_to_update)
        country_to_add_to = Country.query.filter_by(name=form.created_in_country.data).first()
        if not country_to_add_to:
            country_to_add_to = Country(name=form.created_in_country.data)
            db.session.add(country_to_add_to)
        film_to_update.country = country_to_add_to
        country_to_add_to.films_produced.append(film_to_update)
        db.session.commit()
        return redirect(url_for('films_bp.homepage'))
    return render_template('editFilm.html', form=form, film_to_update=film_to_update)
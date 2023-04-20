from flask import render_template, redirect, url_for
from app import app, db
from app.films import films_bp
from app.films.forms import AddDirectorForm, AddFilmForm
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

        category_to_add_to = Category.query.filter_by(name=film_form.categories.data).first()

        film = Film(title=film_form.title.data, 
                    release_date=film_form.release_date.data,
                    created_in_country=country_to_add_to
                    )
        film.category.append(category_to_add_to)
        country_to_add_to.films_produced.append(film)
        country_to_add_to.save_country()
        
    
        category_to_add_to.films.append(film)
        category_to_add_to.save_category()

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
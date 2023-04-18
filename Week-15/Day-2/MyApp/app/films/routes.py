from flask import render_template, redirect, url_for
from app import app
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
    form = AddFilmForm()
    if form.validate_on_submit():
        country_to_add_to = Country.query.filter_by(name=form.created_in_country.data).first()
        if not country_to_add_to:
            country_to_add_to = Country(name=form.created_in_country.data)

        director_to_add_to = Director.query.filter_by(name=form.director.data).first()
        if not director_to_add_to:
            director_to_add_to = Director(name=form.director.data)

        category_to_add_to = Category.query.filter_by(name=form.categories.data).first()
        if not category_to_add_to:
            category_to_add_to = Category(name=form.categories.data)

        film = Film(title=form.title.data, 
                    release_date=form.release_date.data,
                    created_in_country=country_to_add_to,
                    # available_in_countries=[form.available_in_countries.data],
                    category=[category_to_add_to],
                    director=[director_to_add_to]
                    )
        
        country_to_add_to.films_produced.append(film)
        country_to_add_to.save_country()

    
        director_to_add_to.films.append(film)
        director_to_add_to.save_director()
        
    
        category_to_add_to.films.append(film)
        category_to_add_to.save_category()

        film.save_film()
        return redirect(url_for('films_bp.homepage'))
    return render_template('addFilm.html', form=form)

@films_bp.route('/addDirector', methods=('GET', 'POST'))
def addDirector():
    form = AddDirectorForm()
    if form.validate_on_submit():
        director = Director(name=form.name.data)
        director.save_director()
        return redirect(url_for('films_bp.homepage'))
    return render_template('addDirector.html', form=form)
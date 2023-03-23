import flask
from app import app
from app.forms import AddCity
import json

list_of_cities = []


@app.route('/', methods=('GET', 'POST'))
def home():
    form = AddCity()
    if form.validate_on_submit():
        name        = form.cityName.data
        country     = form.cityCountry.data
        inhabitants = form.inhabitants.data
        cityArea    = form.cityArea.data
        latitude    = form.latitude.data
        longitude   = form.longitude.data
        capital     = form.capital.data
        data = {
            'name':name,
            'country':country,
            'inhabitants':inhabitants,
            'cityArea':cityArea,
            'latitude':latitude,
            'longitude':longitude,
            'capital':capital
        }
        list_of_cities.append(data)
        with open('Week-12/Day-2/ExercisesXP/app/cities_around_the_world.json', 'r+') as f:
            file = json.load(f)
            file["list of cities"].append(data)
            f.seek(0)
            json.dump(file, f, indent=2)
    return flask.render_template('index.html', form=form, list_of_cities=list_of_cities)


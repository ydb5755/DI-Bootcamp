import flask
from app import app
from app.forms import MakeCV




@app.route('/', methods=('GET', 'POST'))
def home():
    form = MakeCV()
    if form.validate_on_submit():
        firstName   = form.firstName.data
        lastName    = form.lastName.data
        age         = form.age.data
        experience  = form.experience.data
        data = {
            'firstName':firstName,
            'lastName':lastName,
            'age':age,
            'experience':experience
        }
        return flask.render_template('userCV.html', data=data)
    return flask.render_template('index.html', form=form)
import flask
from app import app
from app.forms import Form


@app.route('/', methods=('GET', 'POST'))
def home():
    form = Form()
    print('before')
    if form.validate_on_submit():
        print('inside')
        print(form.age.data)
        print(form.firstName.data)
        print(form.lastName.data)
    print('after')
    return flask.render_template('index.html', form=form)
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired
from app import app
from app.models import Country, Film, Category, Director

with app.app_context():
    directors  = Director.query.all()

def correct_choices():
    pass    

class AddFilmForm(FlaskForm):
    title                  = StringField('Title', validators=[DataRequired()])
    release_date           = DateField('Release Date', validators=[DataRequired()])
    created_in_country     = StringField('Created in Country:', validators=[DataRequired()])
    # available_in_countries = StringField('Available in Countries:')
    categories             = StringField('Categories', validators=[DataRequired()])
    director               = StringField('Directors', validators=[DataRequired()])
    submit                 = SubmitField('Submit') 

class AddDirectorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit                 = SubmitField('Submit') 
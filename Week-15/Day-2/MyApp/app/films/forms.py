from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired
from app import app
from app.models import Country, Film, Category, Director

with app.app_context():
#     countries  = Country.query.all()
#     films      = Film.query.all()
#     categories = Category.query.all()
    directors  = Director.query.all()

def correct_choices():
    pass    

class AddFilmForm(FlaskForm):
    title                  = StringField('Title', validators=[DataRequired()])
    release_date           = DateField('Release Date', validators=[DataRequired()])
    created_in_country     = StringField('Created in Country:')
    available_in_countries = StringField('Available in Countries:')
    categories             = StringField('Categories')
    director               = SelectField('Director', choices=[direct.name for direct in directors])
    # created_in_country     = SelectField('Country', choices=[country.name for country in countries])
    # available_in_countries = SelectMultipleField('Available in countries:', choices=[country.name for country in countries])
    # category               = SelectMultipleField('Categories', choices=[category.name for category in categories])
    # director               = SelectMultipleField('Directors', choices=[direct.name for direct in directors])
    submit                 = SubmitField('Submit') 

class AddDirectorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit                 = SubmitField('Submit') 
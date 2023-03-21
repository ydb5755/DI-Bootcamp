import flask_wtf
import wtforms
from app.validators import my_length_validator, positive_validator


class AddCity(flask_wtf.FlaskForm):
    cityName    = wtforms.StringField('City Name',[my_length_validator, wtforms.validators.DataRequired()])
    cityCountry = wtforms.StringField('City Country', [wtforms.validators.DataRequired()])
    inhabitants = wtforms.IntegerField('Number of inhabitants',[positive_validator, wtforms.validators.DataRequired()])
    cityArea    = wtforms.IntegerField('Area of city in square kilometers')
    latitude    = wtforms.IntegerField('Enter the city latitude')
    longitude   = wtforms.IntegerField('Enter the city longitude')
    capital     = wtforms.BooleanField('Is this city a capitol?')
    submit      = wtforms.SubmitField('Submit')
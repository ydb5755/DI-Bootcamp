from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, SelectMultipleField, FormField
from wtforms.validators import DataRequired
from app import app
from app.models import Country, Film, Category, Director

with app.app_context():
    all_categories  = Category.query.all()
# all_categories = []

class AddFilmForm(FlaskForm):
    title                  = StringField('Title', validators=[DataRequired()])
    release_date           = DateField('Release Date', validators=[DataRequired()])
    categories             = SelectField('Categories', choices=[cat.name for cat in all_categories] ,validators=[DataRequired()])
    created_in_country     = StringField('Created in Country:', validators=[DataRequired()])
    submit                 = SubmitField('Submit') 

class AddDirectorForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name  = StringField('Last Name', validators=[DataRequired()])
    film       = SelectField('Film', validators=[DataRequired()])
    submit = SubmitField('Submit') 

 

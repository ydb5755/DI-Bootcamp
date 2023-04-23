from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, SelectMultipleField, FormField
from wtforms.validators import DataRequired, StopValidation
from wtforms import widgets
from app import app
from app.models import Country, Film, Category, Director

with app.app_context():
    all_categories  = Category.query.all()
# all_categories = []
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(html_tag='ol', prefix_label=False)
    option_widget = widgets.CheckboxInput()

class MultiCheckboxAtLeastOne():
    def __init__(self, message=None):
        if not message:
            message = 'At least one option must be selected.'
        self.message = message

    def __call__(self, form, field):
        if len(field.data) == 0:
            raise StopValidation(self.message)

class AddFilmForm(FlaskForm):
    title                  = StringField('Title', validators=[DataRequired()])
    release_date           = DateField('Release Date', validators=[DataRequired()])
    categories             = MultiCheckboxField('Categories', choices=[cat.name for cat in all_categories], validators=[MultiCheckboxAtLeastOne()])
    created_in_country     = StringField('Created in Country:', validators=[DataRequired()])
    submit                 = SubmitField('Submit') 

class AddDirectorForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name  = StringField('Last Name', validators=[DataRequired()])
    film       = SelectField('Film', validators=[DataRequired()])
    submit = SubmitField('Submit') 

class UpdateDirectorForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name  = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Submit') 
 

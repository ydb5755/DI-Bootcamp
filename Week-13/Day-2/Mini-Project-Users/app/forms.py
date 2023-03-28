from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import SubmitField, StringField


class UserForm(FlaskForm):
    # jf = FileField('Upload your json file here', validators=[FileAllowed(['json'])])
    name      = StringField('Username')
    street    = StringField('Street')
    city      = StringField('City')
    zipcode   = StringField('Zipcode')
    submit    = SubmitField('Add User')

class LoginForm(FlaskForm):
    name   = StringField('Username')
    city   = StringField('City')
    submit = SubmitField('Login')
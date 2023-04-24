from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, SelectMultipleField, FormField, PasswordField, BooleanField
from wtforms.validators import DataRequired, StopValidation, EqualTo
from wtforms import widgets


class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Re-enter Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up!')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit   = SubmitField('Login')
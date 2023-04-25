from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, EmailField, BooleanField
from wtforms.validators import DataRequired


class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    profile_type = SelectField('Profile Type', choices=['Wookie', 'Hutt', 'Jedi', 'Sith'], validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Re-enter password', validators=[DataRequired()])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')



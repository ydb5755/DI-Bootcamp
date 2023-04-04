from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from portfolio.models import Blog
from portfolio import app

with app.app_context():
    list_of_blogs = Blog.query.all()

class MessageForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    subject = StringField('Subject')
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Contact me!')

class BlogSignUpForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    blog = SelectField('Blog', choices=[blog.name for blog in list_of_blogs])
    submit = SubmitField('Sign up!')
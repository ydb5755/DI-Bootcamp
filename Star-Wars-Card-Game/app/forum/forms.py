from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class ThreadForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    submit = SubmitField('Post to forum')

class CommentForm(FlaskForm):
    content = TextAreaField('Write your comment here')
    submit = SubmitField('Submit comment')
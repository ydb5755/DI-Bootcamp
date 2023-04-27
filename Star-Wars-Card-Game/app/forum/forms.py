from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class ThreadForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    submit = SubmitField('Post to forum')

class CommentForm(FlaskForm):
    content = TextAreaField('Write your comment here', validators=[DataRequired()])
    parent_thread = StringField('parent')
    submit = SubmitField('Submit comment')
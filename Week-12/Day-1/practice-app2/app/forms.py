import flask_wtf
import wtforms

class Form(flask_wtf.FlaskForm):
    firstName     = wtforms.StringField("First Name")
    lastName = wtforms.StringField("Last Name")
    age      = wtforms.StringField("Age")
    submit   = wtforms.SubmitField("Submit")
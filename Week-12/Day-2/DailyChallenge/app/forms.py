import flask_wtf
import wtforms


class MakeCV(flask_wtf.FlaskForm):
    firstName   = wtforms.StringField('First Name',[wtforms.validators.DataRequired()])
    lastName    = wtforms.StringField('Last Name', [wtforms.validators.DataRequired()])
    age         = wtforms.IntegerField('Age',[wtforms.validators.DataRequired()])
    experience  = wtforms.TextAreaField('Experience')
    submit      = wtforms.SubmitField('Submit')
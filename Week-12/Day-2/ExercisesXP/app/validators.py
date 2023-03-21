import wtforms

def my_length_validator(form, field):
    if len(field.data) > 15:
        raise wtforms.ValidationError('Field needs to be less than 15 characters')

def positive_validator(form, field):
    if field.data < 0:
        raise wtforms.ValidationError('This needs to be a positive number')
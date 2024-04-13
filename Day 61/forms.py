from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError

# def my_length_check(form, field):
#     if len(field.data) > 8:
#         raise ValidationError('Password should be at least 8 characters long')

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label=('Password'), 
        validators=[DataRequired(), Length(min=8, message='Field must be atleast 8 characters long')])
    submit = SubmitField(label='Log In')

    
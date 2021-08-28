from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.models import User

def name_exists(form, field):
    name = User.query.filter_by(user_name=field.data).first()
    if name:
        raise ValidationError('Username already exists!')

class RegistrationForm(FlaskForm):
    name = StringField("Enter ur name: ", validators=[DataRequired(), name_exists, Length(3, 15, message='Length must be between 3 to 15 characters')])
    email = StringField('Enter ur Email id: ', validators=[DataRequired()])
    password = PasswordField("Enter password: ", validators=[DataRequired(), Length(5), EqualTo('confirm', message='password must match')])
    confirm = PasswordField("Confirm password: ", validators=[DataRequired()])
    register = SubmitField("Register")

class LoginForm(FlaskForm):
    name = StringField('Enter username', validators=[DataRequired()])
    password = PasswordField('Enter password', validators=[DataRequired()])
    stay_logged_in = BooleanField('Remember me ')
    login = SubmitField("Log in")


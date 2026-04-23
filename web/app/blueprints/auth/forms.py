from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length
from wtforms.fields import PasswordField, StringField

class LoginForm(FlaskForm):
    credential = StringField('Přihlašovací jméno/Emailová adresa', validators=[DataRequired()])
    password = PasswordField('Heslo', validators=[DataRequired()])

class RegistrationForm(FlaskForm):
    username = StringField('Přihlašovací jméno', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Heslo', validators=[DataRequired()])

class VerifyForm(FlaskForm):
    code = StringField('Kód', validators=[DataRequired(), Length(min=6, max=6)])
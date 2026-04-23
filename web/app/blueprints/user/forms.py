from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class CredentialsForm(FlaskForm):
    old_password = PasswordField("Momentální heslo", validators=[DataRequired()])
    new_username = StringField("Nové uživatelské jméno")
    new_password = PasswordField("Nové heslo")
    new_password_integrity = PasswordField(
        "Znovu nové heslo",
        validators=[EqualTo('new_password', message='Hesla se musí shodovat')]
    )
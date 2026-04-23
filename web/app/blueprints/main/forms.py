from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class FilterForm(FlaskForm):
    hours = IntegerField(
        "Hodiny",
        default=1,
        validators=[
            DataRequired(message="Pole nesmí být prázdné."),
            NumberRange(min=1, max=5, message="Prosím, zadejte počet hodin mezi 1 a 5.")
        ]
    )

class ChannelFilterForm(FlaskForm):
    submit = SubmitField("Uložit")
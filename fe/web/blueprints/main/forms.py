from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField, SelectField
from wtforms.validators import DataRequired, NumberRange, Length, Optional

class FilterForm(FlaskForm):
    hours = IntegerField(
        "Hodiny",
        default=1,
        validators=[
            DataRequired(message="Pole nesmí být prázdné."),
            NumberRange(min=1, max=72, message="Prosím, zadejte počet hodin mezi 1 a 72.")
        ]
    )

    order_by_likes = SelectField(
        "Seřadit podle",
        choices=[("true", "Počet Liků"), ("false", "Nejnovější")],
        default="true"
    )

    query = StringField(
        "Hledat:",
        default=None,
        validators=[Optional(), Length(max=30, message="Maximálně 30 znaků.")]
    )

class ThemesFilterForm(FlaskForm):
    hours = IntegerField(
        "Hodiny",
        default=36,
        validators=[
            DataRequired(message="Pole musí být vyplněné."),
            NumberRange(min=1, max=72, message="Hodiny musí být v rozmezí 1-72.")
        ]
    )

class ChannelFilterForm(FlaskForm):
    submit = SubmitField("Uložit")
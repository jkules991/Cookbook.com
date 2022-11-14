from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class RnameForm(FlaskForm):
    name = StringField("Recipe Name:")
    ingredients = StringField("Ingredients:")
    portions = IntegerField("How many portions:")
    instructions = StringField("Instructions:")
    prep_time = IntegerField("How long to prepare and cook:")
    submit = SubmitField("Submit")
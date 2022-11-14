from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class RnameForm(FlaskForm):
    name_form = StringField("Recipe Name:")
    ingredients_form = StringField("Ingredients:")
    prep_t_form = IntegerField("How long to prepare:")
    cook_t_form = IntegerField("How long to cook:")
    submit = SubmitField("Submit")

class RprepForm(FlaskForm):
    cook_method_form = StringField("How long to cook:")
    prep_method_form = StringField("How long to prepare:")
    portions_form = StringField("How many portions:")
    submit = SubmitField("Submit")
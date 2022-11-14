from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class RnameForm(FlaskForm):
    name_form = StringField("Recipe Name:")
    ingredients_form = StringField("Ingredients:")
    prep_t_form = IntegerField("How long to prepare (minutes):")
    cook_t_form = IntegerField("How long to cook (minutes):")
    submit = SubmitField("Submit")

class RprepForm(FlaskForm):
    cook_method_form = StringField("Cooking instructions:")
    prep_method_form = StringField("Preparation:")
    portions_form = StringField("How many portions:")
    submit = SubmitField("Submit")
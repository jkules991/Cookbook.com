from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField

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

class SearchForm(FlaskForm):
    s_name_form= StringField("Recipe Name:")
    s_prep_t_form = IntegerField("How long to prepare (minutes):")
    s_cook_t_form = IntegerField("How long to cook (minutes):")
    s_portions_form = IntegerField("How many portions:")
    submit = SubmitField("Submit")
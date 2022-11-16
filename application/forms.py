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
    list = SelectField("Search by: ", choices=['--Choose Option--','Name','Preparation time','Cooking time','Number of portions'])
    submit = SubmitField("Submit")

class ResForm(FlaskForm):
    name_res = StringField("Recipe Name:")
    prep_t_res = IntegerField("How long to prepare (minutes):")
    cook_t_res = IntegerField("How long to cook (minutes):")
    portions_res = IntegerField("How many portions:")
    submit = SubmitField("Submit")

class EditForm(FlaskForm):
    name_edit_form = StringField("Recipe Name:")
    ing_edit_form = StringField("Ingredients:")
    prep_edit_form = IntegerField("How long to prepare (minutes):")
    cook_edit_form = IntegerField("How long to cook (minutes):")
    cook_method_edit_form = StringField("Cooking instructions:")
    prep_method_edit_form = StringField("Preparation:")
    portions_edit_form = IntegerField("How many portions:")
    submit = SubmitField("Submit")


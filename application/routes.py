from application import app, db
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from application.forms import RnameForm, RprepForm, SearchForm
from application.models import Recipes, Instructions

# creates home page
@app.route('/', methods=["GET"])
@app.route('/home', methods=["GET"])
def home_page():
    return render_template('homepage.html')

@app.route('/create', methods=["GET","POST"])
def create_page():

    pyrecipe_n= RnameForm()
    #Take input from POST
    if request.method == 'POST':
        if pyrecipe_n.validate_on_submit():
                addrecipe = Recipes(r_name=pyrecipe_n.name_form.data, 
                ingredients=pyrecipe_n.ingredients_form.data,
                prep_t=pyrecipe_n.prep_t_form.data,
                cook_t=pyrecipe_n.cook_t_form.data)

                db.session.add(addrecipe)
                db.session.commit()

                return redirect(url_for('create_page2'))

    return render_template('create.html', jirecipe_n=pyrecipe_n)

@app.route('/create2', methods=["GET","POST"])
def create_page2():
    pyprep= RprepForm()
    rec= Recipes.query.order_by(Recipes.id.desc()).first()
    #Take input from POST
    if request.method == 'POST':
        if pyprep.validate_on_submit():
                addInstructions = Instructions(portions=pyprep.portions_form.data, 
                prep_method=pyprep.prep_method_form.data,
                cook_method=pyprep.cook_method_form.data,
                recipe_id= rec.id
                )
                db.session.add(addInstructions)
                db.session.commit()

                return redirect(url_for('home_page'))

    return render_template('create2.html', jiprep=pyprep)

@app.route('/search', methods=["GET","POST"])
def search_page():
    pysearchField= SearchForm()
    if request.method == 'POST':
        if pysearchField.validate_on_submit():
            s_name= pysearchField.s_name_form.data
            prep_d= pysearchField.s_prep_t_form.data
            cook_d= pysearchField.s_cook_t_form.data
            # portion_c= pysearchField.s_portions_form.data
            if s_name != "" and prep_d >= 1 and cook_d >=1:
                s_result= Recipes.query.filter_by(r_name=s_name, prep_t=prep_d, cook_t=cook_d).first()

                return s_result.r_name

    return render_template('search.html', jisearchField=pysearchField)

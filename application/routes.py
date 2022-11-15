from application import app, db
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from application.forms import RnameForm, RprepForm, SearchForm, ResForm
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
            choice_r=pysearchField.list.data
            if choice_r == "Name":
                return redirect(url_for('result_name'))

            elif choice_r == "Preparation time":
                return redirect(url_for('result_prep'))

            elif choice_r == "Cooking time":
                return redirect(url_for('result_cook'))  
            elif choice_r == "Number of portions":
                return redirect(url_for('result_portions'))              
            else:
                return "Invalid Option"

            
    return render_template('search.html', jisearchField=pysearchField)

@app.route('/search/result_name', methods=["GET","POST"])
def result_name():
    pyres= ResForm()
    if request.method == 'POST':
        if pyres.validate_on_submit():
            src_name=pyres.name_res.data
            res_name= Recipes.query.filter_by(r_name=src_name).all()
            return render_template('result_name.html',jiresname=res_name, jires=pyres)
    return render_template('result_name.html', jires=pyres)

@app.route('/search/result_prep', methods=["GET","POST"])
def result_prep():
    pyres= ResForm()
    if request.method == 'POST':
        if pyres.validate_on_submit():
            src_prep=pyres.prep_t_res.data
            res_prep= Recipes.query.filter_by(prep_t=src_prep).all()
            return render_template('result_prep.html',jyres_prep=res_prep, jires=pyres)
    return render_template('result_prep.html', jires=pyres)

@app.route('/search/result_cook', methods=["GET","POST"])
def result_cook():
    pyres= ResForm()
    if request.method == 'POST':
        if pyres.validate_on_submit():
            src_cook=pyres.cook_t_res.data
            res_cook= Recipes.query.filter_by(cook_t=src_cook).all()
            return render_template('result_cook.html',jyres_cook=res_cook, jires=pyres)
    return render_template('result_cook.html', jires=pyres)

@app.route('/search/result_portions', methods=["GET","POST"])
def result_portions():
    pyres= ResForm()
    if request.method == 'POST':
        if pyres.validate_on_submit():
            src_portion=pyres.portions_res.data
            res_portion= Instructions.query.filter_by(portions=src_portion).all()
            recipe= [res.recipes for res in res_portion]
            return render_template('result_portions.html',jires_portion=res_portion, jires=pyres, recipe=recipe)
    return render_template('result_portions.html', jires=pyres)

@app.route('/delete<num>', methods=["GET","POST"])
def delete_page(num):
    return "delete"

@app.route('/delete<num>', methods=["GET","POST"])
def edit_page(num):
    return "edit"

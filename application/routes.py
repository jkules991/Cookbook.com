from application import app, db
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from application.forms import RnameForm

# creates home page
@app.route('/', methods=["GET"])
@app.route('/home', methods=["GET"])
def home_page():
    return render_template('homepage.html')

    
@app.route('/search', methods=["GET","POST"])
def search_page():
    return render_template('search.html')

@app.route('/create', methods=["GET","POST"])
def create_page():

    pyrecipe_n= RnameForm()
    return render_template('create.html', jirecipe_n=pyrecipe_n)

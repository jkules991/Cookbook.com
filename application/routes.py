from application import app
from flask import render_template, request, redirect, url_for


# creates home page
@app.route('/', methods=["GET","POST"])
@app.route('/home', methods=["GET","POST"])
def home_page():
    return render_template('homepage.html')

    
@app.route('/search', methods=["GET","POST"])
def search_page():
    return render_template('search.html')

@app.route('/create', methods=["GET","POST"])
def create_page():
    return render_template('create.html')

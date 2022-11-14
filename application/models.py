from application import db

class Recipes(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    r_name = db.Column(db.String(50), unique=True)
    ingredients = db.Column(db.String(10000))
    prep_t = db.Column(db.Integer)
    cook_t = db.Column(db.Integer)
    rec_inst = db.relationship('Instructions', backref='recipes')


class Instructions(db.Model):

     id = db.Column(db.Integer, primary_key=True)
     portions = db.Column(db.Integer)
     prep_method= db.Column(db.String(16000))
     cook_method = db.Column(db.Text(16000))
     recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False, unique=True)
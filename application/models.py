from application import db

class Recipes(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    r_name = db.Column(db.String(50))
    ingredients = db.Column(db.String(10000))
    rec_inst = db.relationship('Instructions', backref='recipes')


class Instructions(db.Model):

     id = db.Column(db.Integer, primary_key=True)
     portions = db.Column(db.Integer)
     c_method = db.Column(db.String(16000))
     prep_t = db.Column(db.Integer)
     recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))
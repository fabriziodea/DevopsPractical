from application import db

class Winners(db.Model):
	raceno = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)
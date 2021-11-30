from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import requests
import json


app = Flask(__name__)

#password = getenv("DATABASE_PASSWORD")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ppword@db:3306/fives'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Winners(db.Model):
	raceno = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)

#db.drop_all()
#db.create_all()


racedict={}
winnername=""

@app.route('/hall')
def hall():
  data1 = Winners.query.all()
  return render_template('hall.html', records=data1)

@app.route("/", methods = ["GET", "POST"])
def race():
    mydict={}
    global racedict
    global winnername
    for i in range(1,9): 
        racer=requests.get("http://service2:5001/randomnames")
#        racer=str(i*9) #prova
#        mydict.update({str(i): racer}) #prova
        mydict.update({str(i): racer.text})

    winner=requests.get("http://service3:5002/winner")
#    winner= str(5) #prova

    mydict.update({str(9):winner.text})
#    mydict.update({str(9):winner}) #prova

    response = requests.post("http://service4:6000/racelist", json=mydict)
#    response = requests.post("http://service4:6000/raceporco", json=mydict)

#    racedict=mydict #prova
    racedict=response.json()
    winnername=racedict.pop('9')



    return render_template("racepage.html", records=racedict.values(), name=winnername)

@app.route("/results/<bet>", methods=["GET", "POST"])
def results(bet):
    newwinner= Winners(name=winnername)
    db.session.add(newwinner)
    db.session.commit()
    if winnername == bet: 
        message= "Congratulations! You won!"
    if winnername != bet:
        message= "Sorry you lost."
    return render_template("results.html", records=racedict.values(), message=message, name=winnername)


if __name__=="__main__":
	app.run(host = "0.0.0.0", port = 5000, debug = True)
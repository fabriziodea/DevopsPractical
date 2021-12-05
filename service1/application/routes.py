from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from os import getenv
import requests
import json
from application.models import Winners
from application import app, db


creature="Donkey"

@app.route('/hall')
def hall():
  data1 = Winners.query.all()
  return render_template('hall.html', records=data1, creature=creature)

@app.route("/", methods = ["GET", "POST"])
def race():
    mydict={}
    racedict={}
    winnername=""
    for i in range(1,9): 
        racer=requests.get("http://service2:5001/randomnames")
        mydict.update({str(i): racer.text})
    winner=requests.get("http://service3:5002/winner")
    mydict.update({str(9):winner.text})

    response = requests.post("http://service4:6000/racelist", json=mydict)
    racedict=response.json()
    winnername=racedict.pop('9')

    fame=winnername+' '+creature
    newwinner= Winners(name=fame)
    db.session.add(newwinner)
    db.session.commit()

    return render_template("racepage.html", records=racedict.values(), creature=creature)

@app.route("/results/<bet>", methods=["GET", "POST"])
def results(bet):

    data=Winners.query.order_by(desc(Winners.raceno)).first()
    winnername = data.name
    betname = bet+' '+creature
    if winnername == betname: 
        message= "Congratulations! You won!"
    if winnername != betname:
        message= "Sorry you lost."
    return render_template("results.html", message=message, name=winnername)

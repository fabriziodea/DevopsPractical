from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import requests
import json
from application.models import Winners
from application import app, db


creature="Donkey"
racedict={}
winnername=""

@app.route('/hall')
def hall():
  data1 = Winners.query.all()
  return render_template('hall.html', records=data1, creature=creature)

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

#    racedict=mydict #prova
    racedict=response.json()
    winnername=racedict.pop('9')

    return render_template("racepage.html", records=racedict.values(), name=winnername, creature=creature)

@app.route("/results/<bet>", methods=["GET", "POST"])
def results(bet):
    global racedict
    global winnername
    fame=winnername+' '+creature
    newwinner= Winners(name=fame)
    db.session.add(newwinner)
    db.session.commit()
    if winnername == bet: 
        message= "Congratulations! You won!"
    if winnername != bet:
        message= "Sorry you lost."
    return render_template("results.html", records=racedict.values(), message=message, name=winnername, creature=creature)

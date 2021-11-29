from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import requests
import json


app = Flask(__name__)
db = SQLAlchemy(app)

# Replace [PASSWORD] with the root password for your mysql container
password = getenv("DATABASE_PASSWORD")
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{password}@fabsql:3306/fives'

class Winners(db.Model):
	raceno = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)
    def __repr__(self):
        return ''.join(['race number: ', str(self.raceno), '\r\n', 'Winner: 'self.name, '\n'])


@app.route('/')
def hello():
  data1 = Winners.query.all()
  return render_template('hall.html', data1=data1)

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)




racedict={}
winnername=""

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
    betname=bet
    if winnername == betname: 
        message= "Congratulations! You won!"    
    if winnername != betname:
        message= "Sorry you lost."
    return render_template("results.html", records=racedict.values(), message=message, name=winnername)


if __name__=="__main__":
	app.run(host = "0.0.0.0", port = 5000, debug = True)
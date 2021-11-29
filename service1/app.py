from flask import Flask, render_template, request, redirect, jsonify
import requests
import json


app = Flask(__name__)


racers=[]


@app.route("/", methods = ["GET", "POST"])
#@app.route("/") #prova
def race():
    myzip=[]
    mydict={}
    for i in range(1,9): 
        racer=requests.get("http://service2:5001/randomnames")
#        racer=str(i*9) #prova
        racers.append(racer)
        myzip.append(str(i))
        mydict.update({str(i): racer})
    winner=requests.get("http://service3:5002/winner")
#    winner= str(5) #prova

    racers.append(winner)
    myzip.append(str(9))
    mydict.update({str(9):winner})

#    jsonpost=json.dumps(mydict)

#    mydict=dict(zip(myzip,racers))
#    mydict={"1":"11", "2":"22", "3":"33", "4":"34", "5":"55", "6":"86", "7":"77", "8":"88", "9":"0"}
#    mydict={myzip[0]:racers[0],myzip[1]:racers[1],myzip[2]:racers[2],myzip[3]:racers[3],myzip[4]:racers[4],myzip[5]:racers[5],myzip[6]:racers[6],myzip[7]:racers[7],myzip[8]:racers[8]}
    response = requests.post("http://service4:6000/racelist", json=mydict)
#    response = requests.post("http://service4:6000/raceporco", json=mydict)

    racedict=response.json()

#    return newdict["dio"]
    return render_template("racepage.html", records=racedict.values())
#    return render_template("racepage.html", records=racenames)

#@app.route("/results/<int:bet>", methods=["GET", "POST"])
#def results(bet):
#    winner=int(request.get("http://service3:5002/winner"))
#    if winner == bet 
#        render template youwon.html
#    if winner != bet
#        render template youlost.html


if __name__=="__main__":
	app.run(host = "0.0.0.0", port = 5000, debug = True)
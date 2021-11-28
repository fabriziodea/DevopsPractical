from flask import Flask, render_template, request, redirect, jsonify
import requests
import json


app = Flask(__name__)


racers=[]


@app.route("/", methods = ["GET", "POST"])
#@app.route("/") #prova
def race():
    myzip=[]
    for i in range(1,8): 
        racer=requests.get("http://service2:5001/randomnames")
#        racer=str(i*11) #prova
        racers.append(racer)
        myzip.append(str(i))
    winner=requests.get("http://service3:5002/winner")
#    winner='6' #prova
    #winner is text
    racers.append(winner)
    myzip.append(str(9))
#    print(*racers) #prova
    mydict=dict(zip(myzip,racers))

#    mydict={"rawstring":racers}
#    myjson= json.dumps(mydict)
    response = requests.post("http://service4:6000/racelist", json=mydict)
    racenames=response.json()["racelist"]
#    racenames=racers #prova


    return render_template("racepage.html", records=racenames)

#@app.route("/results/<int:bet>", methods=["GET", "POST"])
#def results(bet):
#    winner=int(request.get("http://service3:5002/winner"))
#    if winner == bet 
#        render template youwon.html
#    if winner != bet
#        render template youlost.html


if __name__=="__main__":
	app.run(host = "0.0.0.0", port = 5000, debug = True)
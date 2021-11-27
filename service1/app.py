from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)


racers=[]


@app.route("/", methods = ["POST"])
def race():
    for i in range(1,8): 
        racer=requests.get("http://service2:5001/randomnames")
        racers.append(racer)
    winner=requests.get("http://service3:5002/winner")
    #winner is text
    racers.append(winner)
    response = requests.post("http://service4:5000/racelist", json={'rawstring':racers})
    racenames=response.json()["racelist"]

    return render_template("racepage.html", records=racenames)

#@app.route("/results/<int:bet>", methods=["GET", "POST"])
#def results(bet):
#    winner=int(request.get("http://service3:5002/winner"))
#    if winner == bet 
#        render template youwon.html
#    if winner != bet
#        render template youlost.html


if __name__=="__main__":
	app.run(host = "0.0.0.0", port = 6000, debug = True)
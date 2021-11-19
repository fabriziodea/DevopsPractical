from flask import Flask
import requests

adjective=["mean", "friendly", "aggressive", "smart", "quiet", "noisy", "dangerous", "stubborn", "dirty", "solitary"]
colour=["white", "yellow", "green", "orange", "red", "brown", "pink", "purple", "blue", "black"]

app = Flask(__name__)

@app.route("/")
def race():
    i=0
    challenger=[]
    while i<8:
        rand=requests.get("http://service2:5001/randomnames")
        m=int(rand.text[0])
        n=int(rand.text[1])
        donkey=adjective[m]+' '+colour[n]
        challenger.append(donkey)
        i+=1
    winnertext=requests.get("http://service3:5002/winner")
    winner= int(winnertext.text)    

#    return f"<body style='background-color:{colour};'>\n<h1>dio madonna</h1>"
    return f"{challenger[0]} {challenger[1]} {challenger[2]} {challenger[3]} {challenger[4]} {challenger[5]} {challenger[6]} {challenger[7]}, the winner is {challenger[winner]} "

if __name__=="__main__":
	app.run(host = "0.0.0.0", port = 5000, debug = True)

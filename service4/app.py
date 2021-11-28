from flask import Flask, jsonify, request
import requests

adjective=["mean", "friendly", "aggressive", "smart", "quiet", "noisy", "dangerous", "stubborn", "dirty", "solitary"]
colour=["white", "yellow", "green", "orange", "red", "brown", "pink", "purple", "blue", "black"]

app = Flask(__name__)

@app.route("/")
def race():
    i=0
    race=[]
    while i<8:
        rand=requests.get("http://service2:5001/randomnames")
        m=int(rand.text[0])
        n=int(rand.text[1])
        animal=adjective[m]+' '+colour[n]
        race.append(animal)
        i+=1
    winnertext=requests.get("http://service3:5002/winner")
    winner= int(winnertext.text)    

    animal = race[winner]
    race.append(animal)

    return jsonify({'racelist':race})


@app.route("/racelist", methods=['POST'])
def racelist():
#    rawstring = request.get_json()['rawstring']
    mydict = request.getjson()
    


    rawstring
    first= rawstring[0]

    i=0
    race=[]
    while i<8:
        rand=rawstring[i]
        m=int(rand[0])
        n=int(rand[1])
        animal=adjective[m]+' '+colour[n]
        race.append(animal)
        i+=1
    winner= int(rawstring[8])    

    animal = race[winner]
    race.append(animal)
    return jsonify({'racelist':race})

    



if __name__=="__main__":
	app.run(host = "0.0.0.0", port = 6000, debug = True)

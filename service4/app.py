from flask import Flask, jsonify, request
import requests

adjective=["Mean", "Friendly", "Aggressive", "Smart", "Quiet", "Noisy", "Dangerous", "Stubborn", "Dirty", "Solitary"]
colour=["white", "yellow", "green", "orange", "red", "brown", "pink", "purple", "blue", "black"]

app = Flask(__name__)

@app.route("/raceporco", methods=['POST'])
def race():
    mydict = request.get_json()
    mydict.update({'dio': 'madonna'})

    return jsonify(mydict)


@app.route("/racelist", methods=['POST'])
def racelist():
#    rawstring = request.get_json()['rawstring']
    mydict = request.get_json()
    
#    first= rawstring[0]

    i=1
    race=[]
    myzip=[]
    while i<9:
#        rand=rawstring[i]
        rand= mydict[str(i)]
        m=int(rand[0])
        n=int(rand[1])
        animal=adjective[m]+' '+colour[n]
        race.append(animal)
        myzip.append(str(i))
        i+=1

#    winner= int(rawstring[8])
    winner = int(mydict[str(9)]) 
    myzip.append(str(9))   
    animal = race[winner]
    race.append(animal)
    newdict=dict(zip(myzip,race))
    return jsonify(newdict)

    



if __name__=="__main__":
	app.run(host = "0.0.0.0", port = 6000, debug = True)

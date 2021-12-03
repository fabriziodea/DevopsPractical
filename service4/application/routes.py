from application import app
from flask import Flask, request, Response, jsonify

import requests
import json

adjective=["Mean", "Friendly", "Aggressive", "Smart", "Quiet", "Noisy", "Dangerous", "Stubborn", "Dirty", "Solitary"]
colour=["white", "yellow", "green", "orange", "red", "brown", "pink", "purple", "blue", "black"]

@app.route("/racelist", methods=['POST'])
def racelist():
    mydict = request.get_json()
    i=1
    race=[]
    myzip=[]
    while i<9:
        rand= mydict[str(i)]
        m=int(rand[0])
        n=int(rand[1])
        animal=adjective[m]+' '+colour[n]
        race.append(animal)
        myzip.append(str(i))
        i+=1

    winner = int(mydict[str(9)]) 
    myzip.append(str(9))   
    animal = race[winner]
    race.append(animal)
    newdict=dict(zip(myzip,race))
    return jsonify(newdict)

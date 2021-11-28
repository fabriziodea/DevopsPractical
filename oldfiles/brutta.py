from flask import Flask, jsonify
from random import randint
import json


adjective=["mean", "friendly", "aggressive", "smart", "quiet", "noisy", "dangerous", "stubborn", "dirty", "solitary"]
colour=["white", "yellow", "green", "orange", "red", "brown", "pink", "purple", "blue", "black"]

porco = {"porco":colour}
json= json.dumps(porco)

print(json)







"""namesn= str(randint(0,9))+str(randint(0,9))
challenger=[]

print(namesn)

print(str(randint(0,7)))
i=0
while i<8:
    m=int(namesn[0])
    n=int(namesn[1])
    donkey=adjective[m]+' '+colour[n]
    challenger.append(donkey)
    print(donkey)
    i+=1
"""

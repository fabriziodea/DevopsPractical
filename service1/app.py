from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def race():
    racenames= requests.get("http:/")

    return renderstuff racepage.html

@app.route("/results<bet>")
def results():
    winner=int(request.get("http://service3:5002/winner"))
    if winner == bet 
        render template youwon.html
    if winner != bet
        render template youlost.html
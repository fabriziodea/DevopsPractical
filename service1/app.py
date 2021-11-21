from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route("/")
def race():
    racenames= requests.get("http:/")

    return render_template("racepage.html", records=racenames)

@app.route("/results/<int:bet>", methods=["GET", "POST"])
def results(bet):
    winner=int(request.get("http://service3:5002/winner"))
    if winner == bet 
        render template youwon.html
    if winner != bet
        render template youlost.html
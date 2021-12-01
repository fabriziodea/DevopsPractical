from application import app
from flask import Flask, request, Response
import random

@app.route("/randomnames")
def random_names():
    namesn= str(random.randint(0,9))+str(random.randint(0,9))
    return Response(namesn, mimetype='text/plain')
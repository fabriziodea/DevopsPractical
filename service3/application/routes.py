from application import app
from flask import Flask, request, Response
import random

@app.route("/winner")
def winner():
    return Response(str(random.randint(0,7)), mimetype='text/plain')

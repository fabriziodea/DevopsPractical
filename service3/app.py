from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/winner")
def winner():
    return str(randint(0,7))

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5002, debug = True)
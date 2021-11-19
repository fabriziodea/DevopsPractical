from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/randomnames")
def random_names():
    namesn= str(randint(0,9))+str(randint(0,9))
    return namesn

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5001, debug = True)
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import requests
import json

app = Flask(__name__)

#password = getenv("DATABASE_PASSWORD")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ppword@db:3306/fives'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

import application.models
import application.routes
from flask import Flask
from datetime import datetime
from python_tutorial.day import dayname, greeting

app = Flask(__name__)

@app.route("/")
def hello_world():
    return greeting(datetime.now())

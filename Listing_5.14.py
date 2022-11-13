from datetime import datetime

from flask import Flask

from python_tutorial.day import dayname


app = Flask(__name__)

@app.route("/")
def hello_world():
    return greeting(datetime.now())

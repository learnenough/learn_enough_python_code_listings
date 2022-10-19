from flask import Flask
from datetime import datetime
import calendar

app = Flask(__name__)

@app.route("/")
def hello_world():
    dayname = calendar.day_name[datetime.now().weekday()]
    return f"<p>Hello, world! Happy {dayname}.</p>"

from datetime import datetime
import calendar

from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    dayname = calendar.day_name[datetime.now().weekday()]
    return f"<p>Hello, world! Happy {dayname}.</p>"

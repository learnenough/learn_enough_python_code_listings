from datetime import datetime

from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    # UnPythonic location
    DAYNAMES = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    dayname = DAYNAMES[datetime.now().weekday()]
    return f"<p>Hello, world! Happy {dayname}.</p>"

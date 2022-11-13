from datetime import datetime

from flask import Flask

DAYNAMES = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]


app = Flask(__name__)

@app.route("/")
def hello_world():
    dayname = DAYNAMES[datetime.now().weekday()]
    return f"<p>Hello, world! Happy {dayname}.</p>"

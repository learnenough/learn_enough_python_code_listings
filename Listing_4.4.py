from flask import Flask
from datetime import datetime

app = Flask(__name__)
DAYNAMES = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]

@app.route("/")
def hello_world():
    dayname = DAYNAMES[datetime.now().weekday()]
    return f"<p>Hello, world! Happy {dayname}.</p>"

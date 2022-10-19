import os
from flask import Flask, render_template

def create_app(test_config=None):
    """Create and configure the app."""
    app = Flask(__name__, instance_relative_config=True)
    .
    .
    .
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/palindrome")
    def palindrome():
        return render_template("palindrome.html")

    return app

app = create_app()

import os
from flask import Flask, render_template, request
from palindrome.phrase import Phrase

def create_app(test_config=None):
    .
    .
    .
    @app.route("/")
    def index():
        page_title = "Home"
        return render_template("index.html", page_title=page_title)

    @app.route("/about")
    def about():
        page_title = "About"
        return render_template("about.html", page_title=page_title)

    @app.route("/palindrome")
    def palindrome():
        page_title = "Palindrome Detector"
        return render_template("palindrome.html", page_title=page_title)

    @app.route("/check", methods=("POST",))
    def check():
        return request.form

    return app

app = create_app()

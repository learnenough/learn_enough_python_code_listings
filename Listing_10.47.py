import os

from flask import Flask, render_template, request

from palindrome_mhartl.phrase import Phrase


def create_app(test_config=None):
    .
    .
    .
    @app.route("/")
    def index():
        return render_template("index.html", page_title="Home")

    @app.route("/about")
    def about():
        return render_template("about.html", page_title="About")

    @app.route("/palindrome")
    def palindrome():
        return render_template("palindrome.html",
                               page_title="Palindrome Detector")

    @app.route("/check", methods=("POST",))
    def check():
        return request.form

    return app

app = create_app()

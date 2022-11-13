import os

from flask import Flask, render_template


def create_app(test_config=None):
    """Create and configure the app."""
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # Load the instance config, if it exists, when not testing.
        app.config.from_pyfile("config.py", silent=True)
    else:
        # Load the test config if passed in.
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

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

    return app

app = create_app()

#!/usr/bin/env python3
"""
This module contains a basic Flask
application setup with Babel for i18n.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ doc"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route("/")
def index():
    """first page"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
    """
    Runs the Flask application.
    """

#!/usr/bin/python3
"""Launches an online Flask app.

The prog is liste on port 5000 at 0.0.0.0..
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")

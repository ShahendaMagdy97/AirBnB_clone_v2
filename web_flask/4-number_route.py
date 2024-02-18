#!/usr/bin/python3
"""start a flack server listening on port 5000 handling '/'"""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """handling / route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """handling hbnb route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """handling varible routes"""
    return f"C {escape(text.replace('_', ' '))}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """handling varible routes"""
    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_a_number(n):
    """handling numbers only"""
    return f"{escape(n)} is a number"


if __name__ == '__main__':
    """start the server"""
    app.run(host='0.0.0.0', port=5000)

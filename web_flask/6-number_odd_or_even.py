#!/usr/bin/python3
"""start a flack server liste on port 5000 hand '/'"""
from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """handling / route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hand hbnb route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """hand vari route"""
    return f"C {escape(text.replace('_', ' '))}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """hand vari routes"""
    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_a_number(n):
    """handling num only"""
    return f"{escape(n)} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """hand num and pass it to html temp"""
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """hand num and pass it to html temp us if ins temp"""
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == '__main__':
    """start the server"""
    app.run(host='0.0.0.0', port=5000)

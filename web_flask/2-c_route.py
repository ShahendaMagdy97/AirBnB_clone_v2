#!/usr/bin/python3
"""On port 5000, 0.0.0.0 is where the program is listen.

0.0.0.0, port 5000 is the application's listening port.

"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displ 'C' foll by the valu of <te>."""
    change_text = text.replace("_", " ")
    return "C {}".format(change_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

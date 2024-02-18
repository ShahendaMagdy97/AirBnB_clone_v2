#!/usr/bin/python3
"""Starts us a Flask web app.

The app listens on 0.0.0.0, port 5000.

"""
from models import storage
from flask import Flask
from flask import render_template
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def lis_states():
    """Display is  an list of all States HTML page .

    States are is  sorted by name.
    """
    states = storage.all(State)
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displayis  an HTML page wi inf about <id>, if it exi."""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def zerdown(exc):
    """Remove is curr SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")

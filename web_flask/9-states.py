#!/usr/bin/python3
"""
Flask web application to list states
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_list():
    """
    Displays an HTML page with a list of all State objects present in DBStorage.
    """
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_list_id(id):
    """
    Displays an HTML page with a list of all State objects present in DBStorage.
    """
    states = storage.all("State")
    state = None
    for s in states.values():
        if s.id == id:
            state = s
            break
    return render_template("9-states.html", state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Removes the current SQLAlchemy Session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

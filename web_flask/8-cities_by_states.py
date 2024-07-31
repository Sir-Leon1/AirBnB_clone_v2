#!/usr/bin/python3
"""
Flask web application to list states
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/cities_by_state", strict_slashes=False)
def states_list():
    """
    Displays an HTML page with a list of all State objects present in DBStorage.
    """
    states = storage.all("State")
    cities = storage.all("City")
    return render_template("8-cities_by_states.html", states=states, cities=cities)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Removes the current SQLAlchemy Session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

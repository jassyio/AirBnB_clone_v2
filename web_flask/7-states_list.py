#!/usr/bin/python3
"""Importing Flask to run the web app"""
from flask import Flask, render_template
# from models.engine.db_storage import DBStorage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_states():
    """Render state_list html page to display States created"""
    states = storage.all("State").values()  # Assuming State is the model representing states
    sorted_states = sorted(states, key=lambda state: state.name)  # Sort states by name
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown(self):
    """Method to remove current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
 
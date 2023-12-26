#!/usr/bin/python3
""" Script that runs an app with Flask framework """
import os
import sys

# Get the absolute path of the project's root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the project root to the Python path
sys.path.append(project_root)

from flask import Flask, render_template
from models.engine.db_storage import db_storage
from models.state import State
from models.city import City


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def closedb(exc):
    """ to close a database session"""
    db_storage.close()


@app.route('/cities_by_states')
def states_list():
    """ /states_list route """
    states = db_storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    db_storage.reload()
    app.run("0.0.0.0", 5000)

#!/usr/bin/python3
"""task 7"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """display"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return render_template("7-states_list.html", states=states)

@app.teardown_appcontext
def teardown_app():
    """bye"""
    storage.close()

if __name__ == '__main__':
        app.run(host="0.0.0.0", port=5000)

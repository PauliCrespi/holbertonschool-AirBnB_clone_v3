#!/usr/bin/python3
"""api config"""

from models import storage
from api.v1.views import app_views
from flask import Flask
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """close"""
    storage.close()


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    if getenv("HBNB_API_HOST") is not None:
        host = getenv("HBNB_API_HOST")
    if getenv("HBNB_API_PORT") is not None:
        port = getenv("HBNB_API_PORT")
    app.run(host=host, port=port, threaded=True)

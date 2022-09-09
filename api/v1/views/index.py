#!/usr/bin/python3
"""index"""

from api.v1.views import app_views
import json


@app_views.route('/status')
def status():
    """stat"""
    return ({"status": "OK"})

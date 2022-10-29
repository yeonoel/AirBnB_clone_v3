#!/usr/bin/python3
"""Flask route that return status response."""


from flask import jsonify
from api.v1.views import app_views


app_views@route('/status', methods=['GET'])
def status():
    """Return a JSON: "status": "OK"."""
    return (jsonify({"status": "OK"}))

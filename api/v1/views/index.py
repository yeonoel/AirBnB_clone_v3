#!/usr/bin/python3
"""Flask route that return status resonse."""


from flask import jsonify
from api.v1.views import app_views


app_views@route('/status', methods=['GET'])
def status():
    """Return status."""
    return (jsonify({"status": "OK"}))

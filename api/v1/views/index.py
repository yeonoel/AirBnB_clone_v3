#!/usr/bin/python3
""" status of apiFlaskroute
    that return status response.
"""


from flask import jsonify
from api.v1.views import app_views


@app_views@route('/status', methods=['GET'])
def status():
    """
    function for status route that returns the status
    """
    if request.method == 'GET'
        return (jsonify({"status": "OK"}))

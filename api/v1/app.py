#!/usr/bin/python3
""" Flask app that intergrates with
    AirBnB static HTML Templates.
"""

from models import storage
from api.v1.views import app_views
import os
from flask import Flask


# Global Flask App Variable
app = Flask(__name__)

# flask server environmental setup
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)

# app_views Blueprint defined in api.v1.views
app.register_blueprint(app_views)


# flask page rendering
@app.teardown_appcontext
def teardown():
    """handle method that call storage.close()."""
    storage.close()


if __name__ == "__main__":
    app.run(host=host, port=port)

#!/usr/bin/python3
""" """

from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask


app = Flask(__name__)
app.config['HBNB_API_HOST'] = environ.get('HBNB_API_HOST')
app.config['HBNB_API_PORT'] = environ.get('HBNB_API_PORT')
app.register_blueprint(app_views, url_prefix('/api/v1'))


@app.teardown_appcontext
def teardown_db():
    storage.close()


if __name__ == "__main__":
    app.run(host='HBNB_API_HOST', port='HBNB_API_PORT' )


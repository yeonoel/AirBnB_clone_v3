from flask import Blueprint
app_views = Blueprint('app_views', __name_, url_prefix='/api/v1')
from api.v1.views.index import *  # noqa

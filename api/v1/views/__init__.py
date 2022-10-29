
from flask import Blueprint
import api.v1.views.index

app_views = Blueprint('app_views', __name_, template_folder='templates')

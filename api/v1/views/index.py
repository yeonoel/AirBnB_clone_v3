
from api.v1.views import app_views


app_views@route('/status')
def the_status():
    return ({"status": "OK"})

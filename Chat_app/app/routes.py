from app import app
from app import Mqtt_subscribe

@app.route('/')
@app.route('/index')
def index():
    new_value = Mqtt_subscribe.value
    return new_value
from flask.logging import logging as log
from flask import Blueprint
#from app import mongo

pics_definition = Blueprint('pics', __name__, url_prefix='/pics')

@pics_definition.route('/')
def index():
    log.info('Pics are visited')
    #user = mongo.db.users.find_one_or_404({"_id": username})
    return '''
            <h1>pics</h1>
            <ul>
            <li>1</li>
            <li>2</li>
            <li>3</li>
            </ul>
            '''
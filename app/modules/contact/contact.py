from flask.logging import logging as log
from flask import Blueprint

contact_definition = Blueprint('contact', __name__, url_prefix='/contact')

@contact_definition.route('/')
def index():
    log.info('Contact are visited')
    return '''
            <h1>Contact</h1>
            <p>data of contact<p>
            '''
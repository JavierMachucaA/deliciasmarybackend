from flask.logging import logging as log
from flask import Blueprint

auth_definition = Blueprint('auth', __name__, url_prefix='/auth')

@auth_definition.route('/')
def index():
    log.info('Auth are visited')
    return '''
            <h1>Auth route are here</h1>
            '''
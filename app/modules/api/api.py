from app.modules.auth.auth import auth_definition
from app.modules.contact.contact import contact_definition
from app.modules.pics.pics import pics_definition
from flask import Blueprint
from flask import current_app as app
from flask.logging import logging as log

api_definition = Blueprint('api', __name__)

@api_definition.route('/')
def index():
    log.info('Home api are visited')
    return '''
            <h1>Welcome Delicias Mary Backend</h1>
            <p>
            api
            <br>
            ├── index
            <br>
            |
            <br>
            └── pics/
            <br>
            |
            <br>
            └── auth/
            <br>
            |
            <br>
            └── contact/
            </p>
            '''

def config_api(app):
    app.register_blueprint(api_definition)
    app.register_blueprint(pics_definition)
    app.register_blueprint(contact_definition)
    app.register_blueprint(auth_definition)
    

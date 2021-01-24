# pylint: disable=too-few-public-methods,invalid-name,missing-docstring
import os
from logging.config import dictConfig
# LOGGER CONFIG
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

class BaseConfig(object):
    DEBUG = False

    #ENABLED_MODULES = (
        #'auth',
        #'users',
        #'teams',
        #'api',
    #)

    #STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
    # TODO: consider if these are relevant for this project
    CSRF_ENABLED = True

class ProductionConfig(BaseConfig):
    SECRET_KEY = os.getenv('key')
    MONGOURI = os.getenv('CLOUDSML_API_SERVER_SQLALCHEMY_DATABASE_URI')

class DevelopmentConfig(BaseConfig):
    SECRET_KEY = os.getenv('key-dev')
    MONGOURI = os.getenv('deliciasmary-db')
    DEBUG = True
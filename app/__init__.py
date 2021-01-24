from flask import Flask

from flask import jsonify
import os
import sys
import config
from config import dictConfig
from flask.logging import create_logger
from flask.logging import logging as LOG
from flask import Blueprint
from app.modules.api.api import api_definition
from app.modules.api.api import config_api
from mongoengine import Document
from flask_mongoengine import MongoEngine



CONFIG_NAME_MAPPER = {
    'development': 'config.DevelopmentConfig',
    'production': 'config.ProductionConfig',
}

app = Flask(__name__)
log = create_logger(app)
# mongodb://maryadmin:mary@127.0.0.1:27017/deliciasmary?authSource=blog&readPreference=primary&appname=MongoDB%20Compass&ssl=false
app.config['MONGODB_SETTINGS'] = {
    'db': 'deliciasmary',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

def create_app():
    if os.getenv("DEBUG"):
        env = 'development'
    else:
        env = 'production'
    
    try:
        app.config.from_object(CONFIG_NAME_MAPPER[env])
    except ImportError:
        log.error(
            "You have to have `config.py` or `local_config/__init__.py` in order to use "
            "the default 'local' Flask Config. Alternatively, you may set `FLASK_CONFIG` "
            "environment variable to one of the following options: development, production, "
            "testing."
        )
        sys.exit(1)
        raise

    if app.debug:
        log.setLevel(LOG.DEBUG)
    else:
        log.setLevel(LOG.INFO)

class Pics(db.Document):
    picId = db.StringField()
    picName = db.StringField()
    picUrl = db.StringField()

    def to_json(self):
        return {
                "picId": self.picId,
                "namePic": self.picName,
                "picUrl": self.picUrl
                }
    
for p in Pics.objects:
    log.info(jsonify(p))    

#startup
create_app()
config_api(app)

import os, logging

from flask import Flask
from flask_cors import CORS

from app.resources import api_blueprint
from app.database.db import db

def create_app(config, **kwargs):

    app = Flask(__name__, **kwargs)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    app.register_blueprint(api_blueprint)
    app.config.from_object(config)

    logging.basicConfig(level=logging.INFO)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app

#!/bin/python3
from flask import Flask, url_for
from flask_sse import sse

from importlib import import_module

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__, static_folder='base/static')

def register_blueprints(app):
    for module_name in ['osman', 'login']:
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)
    app.register_blueprint(sse, url_prefix='/stream')

def create_app():
    app.config["REDIS_URL"] = "redis://localhost"
    app.config["JWT_SECRET_KEY"] = "kivanc.1234"
    register_blueprints(app)
    jwt = JWTManager(app)
    return app

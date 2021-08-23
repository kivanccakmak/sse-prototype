#!/bin/python3
from flask import Flask, url_for
from flask_sse import sse

from importlib import import_module

app = Flask(__name__, static_folder='base/static')

def register_blueprints(app):
    for module_name in ['osman']:
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)
    app.register_blueprint(sse, url_prefix='/stream')

def create_app():
    app.config["REDIS_URL"] = "redis://localhost"
    register_blueprints(app)
    return app

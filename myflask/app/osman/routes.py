#!/bin/python
from flask import request, jsonify

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from flask import Blueprint

from app import sse

blueprint = Blueprint(
    'osman_blueprint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)

@blueprint.route('/hello', methods=['GET', 'POST'])
def publish_hello():
    data = request.get_json()
    print("here")
    sse.publish(data, type='greeting')
    return jsonify(msg="message sent"), 200

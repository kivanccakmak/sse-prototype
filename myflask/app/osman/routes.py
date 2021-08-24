#!/bin/python
from flask import request, jsonify
from flask_login import login_required, current_user

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

@sse.before_request
@jwt_required()
def check_access():
    channel = request.args.get("channel")
    current_user = get_jwt_identity()
    print(channel)
    print("channel: {}".format(channel))
    print("current_user: {}".format(current_user))

@blueprint.route('/auth_hello', methods=['GET', 'POST'])
@jwt_required()
def publish_auth_hello():
    data = request.get_json()
    print(data)
    current_user = get_jwt_identity()
    sse.publish(data, type='greeting')
    return jsonify(msg="message sent"), 200

@blueprint.route('/hello', methods=['GET', 'POST'])
def publish_hello():
    data = request.get_json()
    print("here")
    sse.publish(data, type='greeting')
    return jsonify(msg="message sent"), 200

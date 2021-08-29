#!/bin/python
import asyncio
import json
import os
from flask import request, jsonify
from flask_login import login_required, current_user
from websockets import connect

from flask_jwt_extended import create_access_token
from flask_jwt_extended import decode_token
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
def check_access():
    token = request.headers["token"]
    print("token: {}".format(token))
    msg = decode_token(token)
    print(msg)

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

# pokayoke.me (main server)
async def hello(uri, data):
    async with connect(uri) as websocket:
        await websocket.send(data)

@blueprint.route('/sio_hello', methods=['GET', 'POST'])
def publish_sio_hello():
    data = request.get_json()
    asyncio.run(hello("ws://localhost:8765", json.dumps(data)))
    return jsonify(msg="message sent"), 200

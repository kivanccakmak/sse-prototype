#!/bin/python
from flask import request, jsonify

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from flask import Blueprint

from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)

blueprint = Blueprint(
    'login_blueprint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)

DB_USER="kivanc"
DB_PASS="1234"

@blueprint.route('/rest/login', methods=['GET', 'POST'])
def mobilelogin():
    data = request.get_json()
    username, password = None, None
    if 'username' in data.keys():
        username = data['username']
    if 'password' in data.keys():
        password = data['password']

    if username != DB_USER:
        return jsonify(msg="user not defined")

    if password != DB_PASS:
        return jsonify(msg="invalid password")

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

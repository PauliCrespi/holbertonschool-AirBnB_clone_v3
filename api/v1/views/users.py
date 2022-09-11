#!/usr/bin/python3
"""user"""

from api.v1.views import app_views
import json
from models import storage
from flask import jsonify, make_response, request, abort
from models.user import User


@app_views.route('/states/users',
                 methods=['GET'], strict_slashes=False)
def userslist():
    """list all users"""
    elem = storage.values(User).all()
    listobj = []
    for obj in elem:
        listobj.append(obj.to_dict())
    return jsonify(listobj)


@app_views.route('/users/<user_id>',
                 methods=['GET'], strict_slashes=False)
def userinfo(user_id):
    elem = storage.get(User, user_id)
    if not elem:
        abort(404)
    return jsonify(elem.to_dict())


@app_views.route('/userse/<user_id>', methods=['DELETE'], strict_slashes=False)
def deluser(user_id):
    """delete user"""
    elem = storage.get(User, user_id)
    if not elem:
        abort(404)
    storage.delete(elem)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/users',
                 methods=['POST'], strict_slashes=False)
def postuser():
    """post user"""
    if not request.json:
        abort(400, description="Not a JSON")
    if 'email' not in request.json:
        abort(400, description="Missing email")
    if 'password' not in request.json:
        abort(400, description="Missing password")
    if not state:
        abort(404)
    req = request.get_json()
    info = User(**req)
    info.save()
    return make_response(jsonify(info.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_user(city_id):
    """put user"""
    req = request.json
    if not req:
        abort(400, description="Not a JSON")
    if not storage.get(User, user_id):
        abort(404)
    badkeys = ['id', 'email', 'created_at', 'updated_at']
    for key, value in req.items():
        if key not in badkeys:
            elem = storage.get(User, user_id)
            setattr(elem, key, value)
    storage.save()
    return make_response(jsonify(elem.to_dict()), 200)

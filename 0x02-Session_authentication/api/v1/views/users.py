#!/usr/bin/env python3
"""
Users view module
"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models.user import User
from api.v1.app import auth


@app_views.route('/users/me', methods=['GET'], strict_slashes=False)
def get_user_me():
    """
    Retrieves the authenticated User
    """
    user = auth.current_user(request)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """
    Retrieves a User
    """
    if user_id == 'me':
        abort(404)
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())

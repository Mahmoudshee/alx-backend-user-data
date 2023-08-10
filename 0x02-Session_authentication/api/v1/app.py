#!/usr/bin/env python3
"""
Main app module
"""

from flask import Flask, make_response, jsonify, request, abort
from os import getenv
from api.v1.views import app_views
from models import db_session, user
from api.v1.auth.auth import Auth
from api.v1.auth.session_auth import SessionAuth
from api.v1.auth.session_exp_auth import SessionExpAuth
from api.v1.auth.session_db_auth import SessionDBAuth

app = Flask(__name__)

app.register_blueprint(app_views)

auth = None

auth_type = getenv('AUTH_TYPE')

if auth_type == "auth":
    auth = Auth()
elif auth_type == "session_auth":
    auth = SessionAuth()
elif auth_type == "session_exp_auth":
    auth = SessionExpAuth()
elif auth_type == "session_db_auth":
    auth = SessionDBAuth()


@app.errorhandler(404)
def not_found(error):
    """
    404 Not Found error handler
    """
    return make_response(jsonify({"error": "Not found"}), 404)


@app.before_request
def before_request():
    """
    Before request handler
    """
    excluded_paths = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/',
        '/api/v1/auth_session/login/'
    ]
    if auth.require_auth(request.path, excluded_paths):
        if auth.authorization_header(request) is None and \
                auth.session_cookie(request) is None:
            abort(401)
        request.current_user = auth.current_user(request)


@app.teardown_appcontext
def close_db(error):
    """
    Close the database connection
    """
    db_session.remove()


if __name__ == '__main__':
    host = getenv('API_HOST', '0.0.0.0')
    port = getenv('API_PORT', '5000')
    app.run(host=host, port=int(port))

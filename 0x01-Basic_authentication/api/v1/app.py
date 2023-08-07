from flask import Flask, jsonify, abort
from flask import Flask, jsonify, abort
from flask import Blueprint, abort
from flask import Flask, abort, request
from api.v1.auth.auth import Auth

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})

auth = None
if os.getenv("AUTH_TYPE") == "auth":
    auth = Auth()

@app.before_request
def before_request():
    if auth is None:
        return

    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']

    if request.path in excluded_paths:
        return

    if not auth.require_auth(request.path, excluded_paths):
        abort(401)

    auth_header = auth.authorization_header(request)
    if auth_header is None:
        abort(401)

    current_user = auth.current_user(request)
    if current_user is None:
        abort(403)

app_views = Blueprint("app_views", __name__)
@app_views.route("/api/v1/forbidden", methods=["GET"])
def forbidden_endpoint():
    abort(403)

app = Flask(__name__)

# Existing code

@app.errorhandler(401)
def unauthorized(error):
    response = jsonify({"error": "Unauthorized"})
    return response, 401

# Existing code

if __name__ == "__main__":
    app.run(host=API_HOST, port=API_PORT)

app = Flask(__name__)

# Existing code

@app.errorhandler(403)
def forbidden(error):
    response = jsonify({"error": "Forbidden"})
    return response, 403

# Existing code

if __name__ == "__main__":
    app.run(host=API_HOST, port=API_PORT)


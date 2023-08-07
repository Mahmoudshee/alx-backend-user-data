from flask import Flask, jsonify, abort
from flask import Flask, jsonify, abort
from flask import Blueprint, abort

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


#!/usr/bin/python3
"""Here application initialization begins: Create an app instance"""

from flask import Flask, jsonify
from flask_cors import CORS
from os import getenv

from api.v1.views import app_views

from models import storage


app = Flask(__name__)

app.register_blueprint(app_views)

CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(exception):
    """Function that's run after each request is handled"""
    storage.close()


@app.errorhandler(404)
def handle_404(exception):
    """Handles the 404 Exception when the app encounters a 404"""
    data = {
        "error": "Not found"
    }

    resp = jsonify(data)
    resp.status_code = 404

    return resp


if __name__ == "__main__":
    app.run(getenv("HBNB_API_HOST", "0.0.0.0"), getenv("HBNB_API_PORT") or 5000)

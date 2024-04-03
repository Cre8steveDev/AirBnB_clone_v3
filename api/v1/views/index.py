#!/usr/bin/python3
"""Index.py to serve as views for the app yaaaah"""

from flask import jsonify
from api.v1.views import app_views

from models import storage


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """
    status route
    :return: response with json
    """
    response_data = {
        "status": "OK"
    }

    resp = jsonify(response_data)
    resp.status_code = 200

    return resp


@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def stats():
    """
    stats of all objs route
    :return: json of all objs
    """
    response_data = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }

    resp = jsonify(response_data)
    resp.status_code = 200

    return resp

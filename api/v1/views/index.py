#!/usr/bin/python3
"""Defining routes and the handling functions 
This one this one just checking 
"""

from flask import make_response
from api.v1.views import app_views


@app_views.route("/status", strict_slashes=False)
def status():
    """Method that handles requests to the /status route under api/v1"""
    return make_response({"status": "OK"})

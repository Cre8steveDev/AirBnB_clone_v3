#!/usr/bin/python3
"""
Defining routes and the handling functions 
This one this one just checking 
"""

from flask import make_response, jsonify
from api.v1.views import app_views


@app_views.route("/status", strict_slashes=False)
def status():
    """Method that handles requests to the /status route under api/v1"""
    response_data = {"status": "OK"}
    response_data = jsonify(response_data)
    
    response_data.status_code = 200
    
    return response_data

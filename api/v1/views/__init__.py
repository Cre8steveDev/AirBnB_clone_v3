#!/usr/bin/python3
"""Package initialization for the views as a package"""

from flask import Blueprint
from api.v1.views.index import *

app_views = Blueprint("appviews", url_prefix="/api/v1")

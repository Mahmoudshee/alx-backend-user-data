#!/usr/bin/env python3
"""
API views
"""

from flask import Blueprint
from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.session_auth import *  # import the new view

app_views = Blueprint('app_views', __name__)

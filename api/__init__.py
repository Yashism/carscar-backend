# api/__init__.py

from flask import Blueprint

api_bp = Blueprint('api_bp', __name__)

from . import routes

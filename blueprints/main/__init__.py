from flask import Blueprint

main_blueprints = Blueprint("main", __name__)

from . import routes
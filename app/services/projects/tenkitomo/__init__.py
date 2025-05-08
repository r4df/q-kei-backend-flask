# tictactoe project
# Created : 25/05/08
###############################
from flask import Blueprint
proj_tenkitomo_bp = Blueprint("proj_tenkitomo_bp", __name__, template_folder="templates", static_folder="static")
from . import routes

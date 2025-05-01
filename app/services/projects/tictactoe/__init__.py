# tictactoe project
# Created : 25/04/30
###############################
from flask import Blueprint
proj_tictactoe_bp = Blueprint("proj_tictactoe_bp", __name__, template_folder="templates", static_folder="static")
from . import routes
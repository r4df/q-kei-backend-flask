from . import proj_tictactoe_bp
from flask import jsonify, request

from .functions import WON_DRAW, MOVE_O, check_winner, get_best_move, get_available_move

@proj_tictactoe_bp.route("/test", methods=["POST"])
def r_test():
    return jsonify({"resp":"test OK!"})

@proj_tictactoe_bp.route("/checkwinner", methods=["POST"])
def r_checkwinner():

    # Acquire data.
    data = request.json

    # Check if player Won
    winner = check_winner(data["board"])
    if winner is not None:
        return jsonify({"winner" : winner}), 200
    
    available_moves = get_available_move(data["board"])
    if len(available_moves) == 0:
        return jsonify({"winner" : WON_DRAW}), 200

    return jsonify({"winner" : None}), 200

@proj_tictactoe_bp.route("/aimove", methods=["POST"])
def r_aimove():

    # Acquire data.
    data = request.json

    # AI making decisions in life...
    best_move = get_best_move(data["board"])
    data["board"][best_move] = MOVE_O

    return jsonify({"board": data["board"]}), 200

from . import home_bp
from flask import render_template
from app import FRONTEND_URL

@home_bp.route("/", methods=["GET"])
def home():

    return render_template("home.html", front_end=FRONTEND_URL)


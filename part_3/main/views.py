from flask import Blueprint, render_template, request
from .helpers import make_prediction

views = Blueprint('views', __name__)

@views.route("/", methods=["GET", "POST"])
def home():

    return render_template("home.html", data={})
import json
from flask import Blueprint, render_template, request, jsonify
from .helpers import make_prediction

handlers = Blueprint('handlers', __name__)

@handlers.route("/stock/<stock>", methods=["GET"])
def handle_stock(stock):
    predictions, actual, future_prediction, dates, error = make_prediction(stock)
    # print(predictions)
    # print(actual)
    # print(dates)
    # return jsonify({"predictions":predictions})
    return jsonify({"stock":stock, "predictions":predictions, "actual": actual, "future_prediction": future_prediction, "dates":dates, "error": error})
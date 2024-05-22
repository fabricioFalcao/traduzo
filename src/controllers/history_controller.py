from flask import Blueprint, jsonify
from models.history_model import HistoryModel

history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/", methods=["GET"])
def history_view():
    histoy = HistoryModel.list_as_json()
    return jsonify(histoy), 200

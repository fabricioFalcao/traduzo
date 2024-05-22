from flask import Blueprint, jsonify, request, render_template
from models.language_model import LanguageModel

translator_controller = Blueprint("translator_controller", __name__)

translation_data = {
    "languages": LanguageModel.list_dicts(),
    "text_to_translate": "O que deseja traduzir?",
    "translate_from": "pt",
    "translate_to": "en",
    "translated": "What do you want to translate?",
}


@translator_controller.route("/", methods=["GET"])
def translator_view():
    return render_template("index.html", data=translation_data)

from flask import Blueprint, request, render_template
from deep_translator import GoogleTranslator

from models.language_model import LanguageModel


translator_controller = Blueprint("translator_controller", __name__)

languages = LanguageModel.list_dicts()


@translator_controller.route("/", methods=["GET"])
def translator_view():

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate="O que deseja traduzir?",
        translate_from="pt",
        translate_to="en",
        translated="What do you want to translate?",
    )


@translator_controller.route("/", methods=["POST"])
def translate():

    text_to_translate = request.form["text-to-translate"]
    translate_from = request.form["translate-from"]
    translate_to = request.form["translate-to"]
    translated = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )

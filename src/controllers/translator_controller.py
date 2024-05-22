from flask import Blueprint, request, render_template
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel
from models.history_model import HistoryModel

translator_controller = Blueprint("translator_controller", __name__)


@translator_controller.route("/", methods=["GET"])
def translator_view():

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
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

    HistoryModel(
        {
            "text_to_translate": text_to_translate,
            "translate_from": translate_from,
            "translate_to": translate_to,
            "translated": translated,
        }
    ).save()

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


@translator_controller.route("/reverse", methods=["POST"])
def reverse_translate():

    text_to_translate = request.form["text-to-translate"]
    translate_from = request.form["translate-from"]
    translate_to = request.form["translate-to"]
    translated = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    HistoryModel(
        {
            "text_to_translate": translated,
            "translate_from": translate_to,
            "translate_to": translate_from,
            "translated": text_to_translate,
        }
    ).save()

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=translated,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=text_to_translate,
    )

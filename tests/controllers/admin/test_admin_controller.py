from src.models.history_model import HistoryModel
from src.models.user_model import UserModel

# from src.database.db import db
import pytest


@pytest.fixture()
def mock_data():
    # db.get_collection("users").drop()
    # db.get_collection("history").drop()

    UserModel(
        {"name": "Pitty", "level": "admin", "token": "token_da_pitty_veia"}
    ).save()

    mock_translation = HistoryModel(
        {
            "text_to_translate": "Ralf! Wolf! Raul!",
            "translate_from": "en",
            "translate_to": "pt",
        }
    ).save()

    return mock_translation.id


def test_history_delete(app_test, mock_data):
    id = mock_data

    response = app_test.delete(
        f"/admin/history/{id}",
        headers={
            "Authorization": "token_da_pitty_veia",
            "User": "Pitty",
        },
    )
    assert response.status_code == 204
    assert HistoryModel.find_one({"_id": id}) is None

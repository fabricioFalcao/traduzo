from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    data_test = HistoryModel.list_as_json()

    assert "Hello, I like videogame" in data_test
    assert "Do you love music?" in data_test

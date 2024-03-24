from src.utils import get_data




def test_get_data():
    data = get_data()
    assert type(data) is list
    assert len(data) > 0


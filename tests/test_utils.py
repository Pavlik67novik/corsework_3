from src.utils import get_data, last_five_operations




def test_get_data():
    data = get_data()
    assert type(data) is list
    assert len(data) > 0

def test_last_five_operation():

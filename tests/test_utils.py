import src.utils
from src.utils import get_data, last_five_operations, format_date, format_card, get_data_format


def test_get_data():
    data = get_data()
    assert type(data) is list
    assert len(data) > 0
    assert get_data() == True

def test_last_five_operation(operations):
    assert [operation["id"] for operation in operations] == [142264268, 873106923]
    assert [operation["state"] for operation in operations] == ["EXECUTED","EXECUTED"]


def test_format_date():
    assert format_date("2019-03-23T01:09:46.296404") == "23.03.2019"
    assert format_date("2018-04-04T17:33:34.701093") == "04.04.2018"

def test_format_card():
    assert format_card("Visa Gold 5999414228426353") == "Visa Gold 5999 41** **** 6353"


def test_get_data_format(operation_one):
    assert type(get_data_format(operation_one)) != list
    assert [operation["description"] for operation in operation_one] == ["Перевод со счета на счет"]



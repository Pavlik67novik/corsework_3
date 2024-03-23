import json

def get_data():

    """ Читаем файл данных"""
    with open("../data/operations.json", encoding="utf-8") as f:
        return json.load(f)

def filter_data(data):
    """Операции с значением ключа state - EXECUTED"""
    filter_operations = [operation for operation in data if "state" in operation and operation["state"] == "EXECUTED"]
    return filter_operations


def last_five_operations(data):
    """Операция сортировки и вывода последних 5 операций"""
    sorted_operations = sorted(data, key=lambda x: x["date"], reverse=True)
    return sorted_operations[:5]


def format_date (date: str):
    """"Перевод даты в формат ДД.ММ.ГГГГ"""
    date_formet = date.split("T")[0].split("-")[::-1]
    return ".".join(date_formet)


def format_card(card: str):
    card = card.split()
    card_number = card.pop()
    card_name = " ".join(card)
    if card_name.lower() == "счет":
        number_secret = "** " + card_number[-4:]
    else:
        number_secret = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return f"{card_name} {number_secret}"


def get_data_format(data):
    operations = [] #пробежаться по списку добавить строик в нужном нам формате
    for operation in data:
        data = format_date(operations["data"])
        if "from" in operation:

            else:

        return operations



data = get_data_format(...)
for operation in data
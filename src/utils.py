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

#Все что ниже проверка кода





#Все что ниже бред (2)
def get_data_format(data):
    """" Вот так показывали на консультации """
    operations = [] #пробежаться по списку добавить строки в нужном нам формате
    #operachii = filter_data(last_five_operations(get_data),filter_data(get_data))
    for operation in data:
        if "from" in operation:
            #operations.append(string)
            data = format_date(operation["date"])
            operation_a = operation["description"]
            from_who = format_card(operation["from"])
            to_who = format_card(operation["to"])
            sum_trans = operation["operationAmount"]["amount"]
            currency = operation["operationAmount"]["currency"]["name"]
            print(f"{data} {operation_a}\n{from_who} --> {to_who}\n{sum_trans} {currency}")
            return operations

        else:
            print("fatal error")
    print(operations)


#data = get_data()
#print(data)
#data = filter_data(data)
#print(data)





#print(get_data_format(get_data))
        #if "from" in operation:
#            operations.append(string)

#            else:

#        return operations
#data = get_data_format(...)    это в мейне
#for operation in data:         это в мейне
    #print(data)                это в мейне


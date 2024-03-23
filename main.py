from src.utils import format_date, filter_data, format_card, last_five_operations, get_data_format, get_data

data = get_data()
data = get_data_format(data)
for operation in data:
    print(data)
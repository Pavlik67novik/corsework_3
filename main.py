from src.utils import get_data, last_five_operations, get_data_format,filter_data


#data = get_data()
data = filter_data(get_data())
print(data)
data = last_five_operations(data)
print(data)
data = get_data_format(data)
print(data)
#for operation in data:
    #print(data)

#data = last_five_operations()
#print(data)
#list_opera = get_data_format(get_data())
#for operation in list_opera:
#    print(operation)



#data = get_data()
#data = get_data_format(data)
#for operation in data:
#   print(data)
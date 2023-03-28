dict1 = {'name': 'Tom', 'Age': 20, 'Gender': 'Male'}

print(dict1.items())         # dict_items([('name', 'Tom'), ('Age', 20), ('Gender', 'Male')])

for key, value in dict1.items():
    print(f'{key} = {value}')


    
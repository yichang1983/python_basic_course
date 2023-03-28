dict1 = {'name': 'Tom', 'Age': 20, 'Gender': 'Male'}

print(dict1.keys())         #dict_keys(['name', 'Age', 'Gender'])

for i in dict1:
    print(i)                  # name Age Gender
    print(dict1['name'])

for key in dict1.keys():
    print(key)              # name Age Gender

list1 = [{'name': 'Tom', 'Age': 20, 'Gender': 'Male'},{'name': 'Nancy', 'Age': 40, 'Gender': 'Female'}]
for i in list1:
    # print(list1)
    # print(i)
    print(i['name'])        #Tom Nancy
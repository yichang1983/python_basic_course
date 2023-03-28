dict1 = {'name': 'Tom', 'Age': 20, 'Gender': 'Male'}

# del 刪除字典或指定的鍵值對（key & value）
# del(dict1)
# print(dict1)        # NameError: name 'dict1' is not defined.

dict2 = {'name': 'Tom', 'Age': 20, 'Gender': 'Male'}

del dict2['name']
print(dict2)            # {'Age': 20, 'Gender': 'Male'}


# clear()
dict3 = {'name': 'Tom', 'Age': 20, 'Gender': 'Male'}
dict3.clear()
print(dict3)            # {}
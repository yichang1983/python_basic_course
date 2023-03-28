dict1 = {'name': 'Tom', 'Age': 20, 'Gender': 'Male'}

# 1. [key]
# print(dict1['name'])        # Tom
# print(dict1['names'])       # KeyError: 'names'

# 2.函數
# 2.1 get ()
print(dict1.get('name'))            # Tom
print(dict1.get('names'))           # None
print(dict1.get('names', 'Lily'))   # Lily

# 2.2 keys () 查找字典中的所有的 key。返回可迭代對象
print(dict1.keys())                 # dict_keys(['name', 'Age', 'Gender'])

# 2.3 values() 查找字典中的所有的 value。返回可迭代對象
print(dict1.values())               # dict_values(['Tom', 20, 'Male'])

# 2.4 items()   查找字典中的所有的 key & value。返回可迭代對象, 裡面的數據是元組，元組數據1是字典的key, 2是字典的value
print(dict1.items())    # dict_items([('name', 'Tom'), ('Age', 20), ('Gender', 'Male')])

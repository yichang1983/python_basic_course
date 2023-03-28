str1 = 'abcd'
list1 = [10, 20, 30, 40]
tuple1 = (100, 200, 300, 400)
dict1 = {'name' : 'John', 'age': 30}

# del 目標或 del(目標)
# del(str1)
# print(str1)                # NameError: name 'str1' is not defined. Did you mean: 'str'?

# del(list1)
# print(list1)               # NameError: name 'list1' is not defined. Did you mean: 'dict1'?
del(list1[0])
print(list1)                 # [20, 30, 40]

# del(tuple1)
# print(tuple1)              # NameError: name 'tuple1' is not defined. Did you mean: 'tuple'?

# del(dict1)
# print(dict1)               # NameError: name 'dict1' is not defined. Did you mean: 'list1'?
del(dict1['age'])
print(dict1)                 # {'name': 'John'}
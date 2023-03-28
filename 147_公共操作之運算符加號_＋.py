list1 = [1, 2]
list2 = [10, 20]

tuple1 = (2, 3)
tuple2 = (20, 30)

dict1 = {'name': 'Tom'}
dict2 = {'age': 30}

# +: 合併

print(list1 + list2)        # [1, 2, 10, 20]
print(tuple1 + tuple2)      # (2, 3, 20, 30)
print(dict1 + dict2)        # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'


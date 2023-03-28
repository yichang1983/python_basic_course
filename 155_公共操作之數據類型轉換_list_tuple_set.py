list1 = ['a', 'b', 'c', 'd', 'e']
tuple1 = (10, 20, 30, 20, 40, 50)
set1 = {100, 200, 300, 400}

# 把 tuple & set 轉成 list
print(list(tuple1))
print(list(set1))

# 把 list & set 轉成 tuple
print(tuple(list1))
print(tuple(set1))

# 把 list & tuple 轉成 set
print(set(list1))
print(set(tuple1))


# 創建有數據的集合 （ set）
set1 = {10, 20, 30, 40, 50, 60}
print(set1)                         # {50, 20, 40, 10, 60, 30}

set2 = {10, 30, 20, 10, 40, 30}
print(set2)                         # {40, 10, 20, 30} 不重覆

set3 = set('abcdefg')
print(set3)                         # {'a', 'e', 'f', 'g', 'd', 'c', 'b'}

set4 = set()
print(type(set4))                   # <class 'set'>

set5 = {}
print(type(set5))                   # <class 'dict'>



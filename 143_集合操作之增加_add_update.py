# # 1.集合是可變類型
# set1 ={10, 20}
# # add()
# set1.add(100)
# print(set1)         # {100, 10, 20}
#
# # 集合有去重覆的功能，如果追加的數據是集合己有數據，則什麼事都不做
# set1.add(10)
# print(set1)          # {100, 10, 20}
#
# set1.add([10, 20, 30])
# print(set1)         # TypeError: unhashable type: 'list'

# update(): 增加的數據是序列（ list ）
set2 = {20, 30, 40, 50}
set2.update([10,20,30])     # {40, 10, 50, 20, 30}
print(set2)

set2.update(10)
print(set2)                 # TypeError: 'int' object is not iterable



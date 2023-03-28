set1 = {10, 20, 30, 40, 50}
# remove(): 刪除指定數據，如果數據不存在報錯
# set1.remove(10)
# print(set1)         # {50, 20, 40, 30}
#
# set1.remove(10)
# print(set1)         # KeyError: 10

# discard(): 刪中指定數據，如果數據不存在不報錯
set2 = {10, 20, 30, 40, 50}
set2.discard(20)
print(set2)            # {50, 40, 10, 30}

set2.discard(20)
print(set2)             # {50, 40, 10, 30}

# pop()： 隨機刪除某個數據，並返回這個數據
set3 = {10, 20, 30, 40, 50}
del_num = set3.pop()
print(del_num)          # 50
print(set3)             # {20, 40, 10, 30}


# 1。拆包元組數據

def return_num():
    return 100, 200

result = return_num()   # 用一個變量去接收返回值
print(result)           # (100, 200) -〉得到的結果

num1, num2 = return_num()   # 用二個變量去接收返回值
print(num1)                 # 100
print(num2)                 # 200

# 2。字典數據拆包：變量存儲的數據是key值
# 先準備字典，然後拆包
dict1 = {'name':'Tom', 'age':30}
a, b = dict1            # 用二個變量去接收，所得到的是key
print(a)                # name
print(b)                # age

# 如果需要得到value，則使用下面的方法
print(dict1[a])         # Tom
print(dict1[b])         # 30

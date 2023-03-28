# 需求：創建字典 key 是 1-5的數字，Value是這個數字的平方
# dict1 = {key: value for i in range(1, 5)}
dict1 = {i: i ** 2 for i in range(1, 5)}         # 最左邊的 i 是 key, 左邊第二個 i 就是 value
print(dict1)

dict2 = {f'key:{k}:value = {k ** 2}' for k in range(1, 5)}
print(dict2)

dict3 = {f'數字:{i}:平方是 = {i ** 2}' for i in range(1, 5)}
print(dict3)
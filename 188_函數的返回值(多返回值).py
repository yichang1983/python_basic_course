# 需求：一個函數有二個返回值 1和2

# 一個函數如果有多個return不能都執行，只執行第一個return:無法做法一個函數多個返回值
# def return_num():
#     return 1
#     return 2
#
# result = return_num()
# print(result)

# 一個函數多個返回值的寫法
def return_num():
    # return 1, 2           # 返回值是元組 -＞ (1, 2)
    # return 後面可以宜接書寫：元組，列表，字典，返回多個值如下面的操作：
    # return (1, 2)         # (1, 2)
    # return[1, 2]            # [1, 2]
    return{'name': 'John', 'age': 30}       # {'name': 'John', 'age': 30}

result = return_num()
print(result)

# 需求: 任意二個數字, 先進行數字處理(絕對值或四拾五入)再求和計算
# 1.寫法一
def add_sum(a, b):
    return abs(a) + abs(b)

result = add_sum(1, 2)
print(result)       # 3

# 2.高階寫法: f 是第三個參數,用來接收將來傳入的函數
def sum_num(a, b, f):
    return f(a) + f(b)

result1 = sum_num(-1.1, 2.5, abs)
print(result1)      # 3.6

result2 = sum_num(1.3, 2.8, round)
print(result2)      # 4

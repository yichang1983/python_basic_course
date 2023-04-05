# reduce(), reduce(func, lst)其中func 必須有2個參數.每次func計算的結果繼續和序列的下一個元素做累積計算
list1 = [1, 2, 3, 4, 5]
# 1. 導入模塊
import functools
# 2. 定義功能函數
def func(a,b):
    return a + b

# 3. 調用reduce作用:功能函數計算的結果和序列的下一個數據做累計計算
result = functools.reduce(func, list1)      # 用functools模塊裡的reduce函數.
print(result)           # 15

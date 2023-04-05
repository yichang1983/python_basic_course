# 需求: 計算list1序列中各個數字的2次方.
# 1. 準備列表數據
list1 = [1, 2, 3, 4, 5]
# 2. 準備2次方計算的函數
def func(x):
    return x ** 2               # 這個是可以自由修改的.

# 3. 調用map
result = map(func,list1)        # 用 func 函數作用到list1.
# 4. 驗收成果
print(result)       # <map object at 0x000001DBEAB33128>

print(list(result))    # [1, 4, 9, 16, 25]  -> 用 list 來把result 轉換.



# filter(), reduce(func, lst)函數用於過濾序列,過濾掉不符合條件的元素,返回一個filter對象.如果要轉換為列表可以使用list ()來轉換.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 1. 定義功能函數,過濾序列中的偶數
def func(x):            # x就是後面要用list1去帶入.
    return x % 2 == 0                        # 這個是可以自由修改的.

# 3. 調用filter
result = filter(func, list1)    # func 就是調用第4行的函數,然而list1就是取代x.
print(result)           # <filter object at 0x0000012FFAA14128>
print(list(result))     # [2, 4, 6, 8, 10]


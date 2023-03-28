a = 10
b = 20
# 1. 方法一
""""
1.1 定義中間的第三變量，為了臨時存儲a 或 b的數據
1.2 把a 的數據存儲到c 做保存
1.3 把b 的數據賦值到a a=20
1.4 把c 的數據賦值到b b=10
"""
c = 0
c = a
a = b
b = c

print(a)
print(b)

# 2. 方法二
c, d = 100, 200     # 用 c 和 d 去儲存 100和 200
print(c)        # 100
print(d)        # 200

d, c = c, d         # 用 d 和 d 去儲存 c 和 d
print(c)        # 200
print(d)        # 100

def fn1():
    return 100
result = fn1()
print(result)          # 100


# 1。 無參數
result = lambda: 100        # 100 指的是 return 的值
print(result())

# 2。 一個參數
result1 = lambda a: a           # 第一個 a 是指形參， 第二個 a 是指return 的值
print(result1('hello world'))   # 這兒的'hello world' 是指實參，代入第八行的形參中。

# 3。 默認參數/缺省參數
result2 = lambda a,b,c=100: a + b + c
print(result2(10, 20))          # 130
print(result2(10, 20, 200))     # 230

# 4。 可變參數： *args
result3 = lambda *args: args
print(result3(10, 20))          # (10, 20) 返回元組
print(result3(10, 20, 30, 40))  # (10, 20, 30, 40)  返回元組
print(result3(10))              # (10,)  返回元組

# 5。 可變參數： **kwargs
result4 = lambda **kwargs: kwargs
print(result4(name='TOM', age=20, gender='Male'))       # {'name': 'TOM', 'age': 20, 'gender': 'Male'} 返回字典。

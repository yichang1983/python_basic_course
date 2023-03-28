# 1. float() -- 將數據轉成浮點型
num1 = 1
str1 = '10'

print(type(float(num1)))
print(float(num1))
print(float(str1))

# 2. str() -- 將數據轉成字串
print(type(str(num1)))

# 3. tuple() -- 將一個序列轉成元組
list1 = [10, 20, 30]
print(tuple(list1))

# 4. list[] -- 將一個序列轉成列表
t1 = (100, 200, 300)
print(list(t1))


# 5. eval() -- 計算在字符串中的有效pythonq表達式,並返回一個對象
str2 = '1'
str3 = '1.1'
str4 = '(1000, 2000, 3000)'
str5 = '[1000, 2000, 3000]'

print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))
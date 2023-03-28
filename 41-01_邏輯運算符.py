a = 0
b = 1
c = 2

# 1. and: 都真才真
print((a < b) and (c > b))
print((a > b) and (c > b))

# 2. or 一真則真, 都假才假
print((a < b) or (c > b))
print((a > b) or (c > b))

# 2. not: 取反
print(not False)

print(not (c > b))

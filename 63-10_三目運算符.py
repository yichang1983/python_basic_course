"""
條件成立執行表達式 if 左邊條件 else 條件不成立執行的表達式(右邊條件)

"""
a = 1
b = 2
c = a if a > b else b

print(c)


aa = 10
bb = 6
cc = aa - bb if aa > bb else bb - aa
print(cc)
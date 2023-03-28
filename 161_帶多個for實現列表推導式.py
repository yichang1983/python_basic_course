# 需求：[(1, 0),(1, 1),(1, 2),(2, 0),(2, 1),(2, 2)]
# 數據1： 1 和 2 range (1,3)
# 數據2： 0，1，2 range (3)

list1 = []
for i in range(1,3):
    for j in range(3):
        list1.append((i, j))
print(list1)

# 多個for 實現列表推導式
list2 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list2)

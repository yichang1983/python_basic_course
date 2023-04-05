students = [
    {'name': 'TOM', 'age': 20},
    {'name': 'John', 'age': 30},
    {'name': 'Nancy', 'age': 28},
]
# sort(key=lambda..., reverse=bool數據)
# 1. name key 對應的值進行升序排序
students.sort(key=lambda a: a['name'])      # 這兒的第1個a (排序的元素, 所有字典) 第2個a (排序的標準則按照 name 去排序)
print(students)     # [{'name': 'John', 'age': 30}, {'name': 'Nancy', 'age': 28}, {'name': 'TOM', 'age': 20}]

# 2. name key 對應的值進行降序排序
students.sort(key=lambda b: b['name'], reverse=True)
print(students)     # [{'name': 'TOM', 'age': 20}, {'name': 'Nancy', 'age': 28}, {'name': 'John', 'age': 30}]


# 3. age key 對應的值進行升序排序
students.sort(key=lambda c: c['age'])
print(students)     # [{'name': 'TOM', 'age': 20}, {'name': 'Nancy', 'age': 28}, {'name': 'John', 'age': 30}]

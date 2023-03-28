counts = {'MBP': 268, 'HP': 125, 'Dell': 201, 'Lenovo': 199, 'Acer': 99}

# 需求：提取電腦台數大於等於 200
# 獲取所有鍵值對數據，判斷value值大於等於 200 返回字典

print(counts.items())       # dict_items([('MBP', 268), ('HP', 125), ('Dell', 201), ('Lenovo', 199), ('Acer', 99)])

dict1 = {key: value for key, value in counts.items() if value >= 200}
print(dict1)
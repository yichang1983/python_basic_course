list1 = ['name', 'age', 'gender', 'id']
list2 = ['Tom', '30', 'Male']

dict1 = {list1[i]: list2[i] for i in range(len(list2))}
print(dict1)

# 總結：
# 1. 如果二個列表數據個數相同， len 統計任何一個列表的長度都可以。
# 2. 如果二個列表數據個數不同， len 統計數據多的列表數據個數會報錯； len統計數據少的列表數據個數不會報錯。
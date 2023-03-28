my_list = ['Tom','Lily','John']

# del   刪除指定下標的數據
# del(my_list)
# print(my_list)      # NameError: name 'my_list' is not defined

# pop() --刪除指定下標的數據,如果不指定標,默認刪除最後一個數據.
# 無論是按照下標還是刪除最後一個, pop 含數都會返回這個被刪除的數據
my_list1 = ['Chen','Huang','John']
new_list1 = my_list1.pop()
print(new_list1)    # John
print(my_list1)     #['Chen', 'Huang']

# remove(數據)
my_list2 = ['Lin','Nancy','John']
my_list2.remove('Nancy')
print(my_list2)            # ['Lin', 'John']

# clear() -- 清空
my_list3 = ['Zhang','Ming','John']
my_list3.clear()
print(my_list3)         #[]

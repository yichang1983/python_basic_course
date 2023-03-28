list = ['Tom','John','Nancy']

# 1.修改指定下標的數據
list[0] = 'aaa'
print(list)             #['aaa', 'John', 'Nancy']

# reverse
list1 = [1,3,2,8,5,7]
list1.reverse()
print(list1)            #[7, 5, 8, 2, 3, 1]

# sort()                #把值升序排列
list2 = [3,2,4,7,0,1,9]
list2.sort()
print(list2)            #[0, 1, 2, 3, 4, 7, 9]

list3 = [3,2,4,7,0,1,9]
list3.sort(reverse=True)    #reverse 把值降序排列
print(list3)            #[9, 7, 4, 3, 2, 1, 0]
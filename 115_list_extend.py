my_list = ['Tom','Lily','John']
print(my_list)       # ['Tom', 'Lily', 'John']
print("------------")
my_list.extend('Nancy')
print(my_list)      # ['Tom', 'Lily', 'John', 'N', 'a', 'n', 'c', 'y']

print("------------")
my_list2 = ['Tom','Lily','John']

my_list2.extend(['Judy','Chad'])
print(my_list2)      # ['Tom', 'Lily', 'John', 'Judy', 'Chad']
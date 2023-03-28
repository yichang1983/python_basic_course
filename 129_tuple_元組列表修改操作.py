t1 = ('aa', 'bb', 'cc', 'dd')

# t1[0] = 'aaa'
# print(t1)       # TypeError: 'tuple' object does not support item assignment

t2 = ('aa', 'bb', ['cc', 'dd'])
print(t2[2])        # ['cc', 'dd']
print(t2[2][1])     # dd

t2[2][1] = "Chen"
print(t2)           # ('aa', 'bb', ['cc', 'Chen'])


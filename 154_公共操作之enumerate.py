# enumerate
list1 = ['a', 'b', 'c', 'd', 'e']

for i in enumerate(list1):
    print(i)                # (0, 'a') (1, 'b') (2, 'c') (3, 'd') (4, 'e')


for b, c in enumerate(list1):
    print(f'下標為{b},數值為{c}') # 下標為0,數值為a 下標為1,數值為b 下標為2,數值為c 下標為3,數值為d 下標為4,數值為e
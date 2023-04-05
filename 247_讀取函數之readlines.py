# readlines
f = open('test.txt', 'r')
result = f.readlines()
print(result)   # ['aaaaa\n', 'bbbbb\n', 'ccccc\n', 'ddddd\n', 'eeeee'] -> 連換行符號\n 都被加進去列表裡.

f.close()
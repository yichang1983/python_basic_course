"""
語法: 文件對象 seek(偏移量, 起始位置) 0開頭 1當蒯 2結尾
目標:
    1. r 改變文件指針位置:改變讀取數據開始位置或把文件指針放結尾(無法讀取數據)
    2. a 改變文件指針位置. 做到可以讀取出來數據
"""
# f = open('test.txt', 'r+')    # r+ 表示讀寫
# f.seek(2,0)     # aaa\n bbbbb\n ccccc\n ddddd\n eeeee
# f.seek(0,2)       # nothing

f = open('test.txt', 'a+')      # a+ 表示讀寫
f.seek(0, 0)

content = f.read()
print(content)

f.close()
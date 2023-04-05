"""
1.訪問模式對文件的影響
2.訪問模式對write()的影響
3.訪問模式是否可以省略
"""
# r:如果文件不存在, 報錯;不支持寫入操作, 表示只讀
# f = open('test.txt', 'r')
# f.write('bbb')            # io.UnsupportedOperation: not writable
# f.close()

# w:只寫,如果文件不存在,新建文件;執行寫入, 會覆蓋原有內容.
# f = open('test1.txt', 'w')
# f.write('ccc')
# f.close()

# a: 追加, 如果文件不存在, 新建文件:
# f = open('test.txt', 'a')
# f.write('xyz')
# f.close()

# 訪問模式參數可以省略, 如果省略表示訪問模式為 r
f = open('test1.txt')
f.close()

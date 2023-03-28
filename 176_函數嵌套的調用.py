# 二個函數 testA 和 testB --- 在 A 裡面嵌套調用 B

# B函數
def testB():
    print('B函數開始-----')
    print('這是B函數')
    print('B函數結束-----')

def testA():
    print('A函數開始-----')
    testB()
    print('A函數結束-----')

testA()

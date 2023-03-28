# 聲明全局變量，函數體內外都能訪問

a = 100
print(a)

def testA():
    print(a)
def testB():
    print(a)

testA()         # 100
testB()         # 100


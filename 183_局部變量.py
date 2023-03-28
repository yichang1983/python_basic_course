# 定義一個函數，聲明一個變量：函數體內部訪問，函數體外部訪問。
def testA():
    a = 100
    print(a)

testA()
print(a)        # 報錯（NameError: name 'a' is not defined） a變量是函數內部的變量，函數外部無法訪問-- a是要個局部變量。



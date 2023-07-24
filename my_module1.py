#需求: 一個函數 完成任意二個數字加法運算
def testA(a,b):
    print(a + b)

# 測試信息
# testA(1, 1)
#
# print(__name__)
#__name__是系統變量,是模塊的標識符,值是:如果自身模塊值是__main__, 否則是當前的模塊的名字
if __name__ == '__main__':
    testA(9,9)
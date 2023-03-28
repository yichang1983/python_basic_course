# 1。定義二個函數。 2。函數一有返回值50：函數二把返回值50作為參數傳入（定義函數二要有形參）

def test1():
    return 50

def test2(num):
    print(num)

result = test1()        #先得到函數一的返回值，再把這個返回值傳入到函數二

test2(result)           # 50


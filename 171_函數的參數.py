# 1.函數：固定數據 1和2 加法
def add_num1():
    result = 1 + 2
    print(result)

add_num1()          # 3


# 2。 參數形式傳入真實數據，做加法運算
def add_num2(a,b):
    result = a + b
    print(result)

add_num2(10,20)         # 30
add_num2(100,200)       # 300
add_num2(100)           # TypeError: add_num2() missing 1 required positional argument: 'b', 定義函數有2個參數，傳入數據也是要2個

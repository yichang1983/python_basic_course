# 需求： 函數返回值 100

# 1。 函數
def fn1():
    return 100
result = fn1()
print(result)          # 100

# 2。lambda 匿名函數
# lambda 參數列表： 表達示
fn2 = lambda: 100
print(fn2)              # <function <lambda> at 0x1037bc7c0>   結果是 lambda 內存地址
print(fn2())            # 100


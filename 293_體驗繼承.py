# 1. 定義父類
class A(object):
    def __init__(self):
        self.num = 1
    def print_info(self):
        print(self.num)

# 2. 定義子類 繼承父類
class B(A):
    pass
# 3. 創建對象, 驗證結論

result = B()
result.print_info()

# 1. 師父類,屬性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[煎餅果子配方]'

    def make_cake(self):
        print(f'use {self.kongfu} to make a delicious biscuit')
# 為了驗證多繼承, 添加School父類
class School(object):
    def __init__(self):
        self.kongfu = '[黑馬煎餅果子配方]'
    def make_cake(self):
        print(f'use {self.kongfu} to make a delicious biscuit')

# 2.定義徒弟類,繼承師父類和學校類
class Prentice(School, Master):         # 這兒繼承了School 和 Master 父類
    pass

# 3.用徒弟類創建對象, 調用實例
aline = Prentice()
print(aline.kongfu)
aline.make_cake()

#結論:如果一個類繼承多個父類, 優先繼承第一個父類的同名屬性和方法
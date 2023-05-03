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

# 2.定義徒弟類,繼承師父類和學校類,添加和父類同名屬性和方法.
class Prentice(School, Master):         # 這兒繼承了School 和 Master 父類
    def __init__(self):
        self.kongfu = '[獨創煎餅果子配方]'
    def make_cake(self):
        print(f'use {self.kongfu} to make a delicious biscuit')

# 3.用徒弟類創建對象, 調用實例
aline = Prentice()
print(aline.kongfu)
aline.make_cake()

#結論:如果子類和父類擁有同名屬性和方法, 子類創建對象調用屬性和方法的時候,調用到的是子類裡面的同名屬性和方法.
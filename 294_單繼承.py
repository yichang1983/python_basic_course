# 1. 師父類,屬性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[煎餅果子配方]'

    def make_cake(self):
        print(f'use {self.kongfu} to make a delicious biscuit')

# 2.定義徒弟類,繼承師父類
class Prentice(Master):
    pass

# 3.用徒弟類創建對象, 調用實例
aline = Prentice()
print(aline.kongfu)
aline.make_cake()
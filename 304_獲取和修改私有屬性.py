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
    def __init__(self):
        self.kongfu = 'special cake'
        self.__money = 20000

    def __info_print(self):
        print('私有方法')
    #定義函數:獲取私有屬性值 get_xx
    def get_money(self):
        return self.__money
    #定義函數:修改私有屬性值 set_xx
    def set_money(self):
        self.__money = 500

# 3.用徒弟類創建對象, 調用實例
aline = Prentice()
#調用獲取私有屬性值 get_xx
print(aline.get_money())
#調用修改私有屬性值 set_xx
aline.set_money()
print(aline.get_money())


# 1. 師父類,屬性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[煎餅果子配方]'

    def make_cake(self):
        print(f'use {self.kongfu} to make a delicious biscuit')
# 為了驗證多繼承, 添加School父類
class School(Master):
    def __init__(self):
        self.kongfu = '[黑馬煎餅果子配方]'
    def make_cake(self):
        print(f'use {self.kongfu} to make a delicious biscuit')

        # 2.1 super(當前類名, self).函數()
        # super(School, self).__init__()
        # super(School, self).make_cake()
        super().__init__()
        super().make_cake()


# 2.定義徒弟類,繼承師父類和學校類,添加和父類同名屬性和方法.
class Prentice(School, Master):         # 這兒繼承了School 和 Master 父類
    # 需求:一次性調用父類 School Master 的方法
    def make_old_cake(self):
        #方法一:如果定義的類名修改, 這裡也要修改,麻煩:代碼量大.
        # School.__init__(self)
        # School.make_cake(self)
        # Master.__init__(self)
        # Master.make_cake(self)
        #方法二: super()
        #2.1 super(當前類名, self).函數()
        # super(Prentice, self).__init__()
        # super(Prentice, self).make_cake()
        #2.2 super().函數()
        super().__init__()
        super().make_cake()




# 3.用徒弟類創建對象, 調用實例

aline = Prentice()
aline.make_cake()
# aline.make_old_cake()



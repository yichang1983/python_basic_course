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
        #加自己的初始化的原因:如果不加這個自己的初始化,kongfu 屬性值是上一次調用的init 內的kongfu屬性值。
        self.__init__()
        print(f'use {self.kongfu} to make a delicious biscuit')
    #子類調用父類的同名方法和屬性:把父類的同名屬性和方法再次封裝
    def master_make_cake(self):
        #父類類名.函數（）
        Master.__init__(self)
        #再次調用初始化的原因:這裡想要調用父類的同名方法和屬性，屬性在init 初始化位置，所以需要再次調用init 。
        Master.make_cake(self)
    def school_make_cake(self):
        School.__init__(self)
        School.make_cake(self)


# 3.用徒弟類創建對象, 調用實例
aline = Prentice()
print(aline.kongfu)
aline.master_make_cake()    # use [煎餅果子配方] to make a delicious biscuit
aline.school_make_cake()    # use [黑馬煎餅果子配方] to make a delicious biscuit
aline.make_cake()           # use [獨創煎餅果子配方] to make a delicious biscuit


#結論:如果子類和父類擁有同名屬性和方法, 子類創建對象調用屬性和方法的時候,調用到的是子類裡面的同名屬性和方法.


# 拓展寫法: 顯示出Prentice 它的繼承關係.
# print(Prentice.__mro__)     #(<class '__main__.Prentice'>, <class '__main__.School'>, <class '__main__.Master'>, <class 'object'>)

# 步驟:1.創建類 Grand_prentice, 用這個類創建對象, 2. 用這個對象調用父類的屬性或方法.
class Grand_prentice(Prentice):
    pass

chen = Grand_prentice()
chen.make_cake()         # use [獨創煎餅果子配方] to make a delicious biscuit
chen.master_make_cake()  # use [煎餅果子配方] to make a delicious biscuit
chen.school_make_cake()  # use [黑馬煎餅果子配方] to make a delicious biscuit

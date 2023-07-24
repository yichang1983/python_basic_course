#1.定義類
class A(object):
    a = 0

    def __init__(self):
        self.b = 1

#2.創建對象
aa = A()
#3.週用__dict__
print(A.__dict__)
print(aa.__dict__)

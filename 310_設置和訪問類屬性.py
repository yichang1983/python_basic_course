#1.定義類,定義類屬性
class Dog(object):
    tooth = 10

#2.創建對象
xiaoming = Dog()
Nancy = Dog()
#3.訪問類屬性:類和對象
print(Dog.tooth)        # 10
print(xiaoming.tooth)   # 10
print(Nancy.tooth)      # 10

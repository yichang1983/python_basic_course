
class Dog(object):
    tooth = 10

xiaoming = Dog()
Nancy = Dog()

#1.類  類.類屬性 = 值
Dog.tooth = 20
print(Dog.tooth)         # 20
print(xiaoming.tooth)    # 20
print(Nancy.tooth)       # 20
#2.測試通過對象修改類屬性
xiaoming.tooth = 1000
print(Dog.tooth)        # 20
print(xiaoming.tooth)   # 1000
print(Nancy.tooth)      # 20



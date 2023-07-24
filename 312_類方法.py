#1.定義類:私有類屬性,類方法獲取這個私有類屬性
class Dog(object):
    __tooth = 10

    #定義類方法
    @classmethod
    def get_tooth(cls):
        return cls.__tooth

#2.創建對象, 調用類方法
result = Dog.get_tooth()
print(result)

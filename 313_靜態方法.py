#1.定義類:定義靜態方法
class Dog(object):
    @staticmethod
    def info_print():
        print('this is a static method')

#2.創建對象
nancy = Dog()
#3.調用靜態戶法: 類和對象
Dog.info_print()        # this is a static method
nancy.info_print()      # this is a static method


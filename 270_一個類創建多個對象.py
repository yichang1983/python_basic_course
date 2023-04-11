# 1. 一個類可以創建多個對象. 2.多個對象都調用函數的時候. self地址是不同的.
class Washer():
    def wash(self):
        print('洗衣服')
        print(self)
Samsung1 = Washer()     # 創建對象 # 對象名 = 類名()
Samsung1.wash()         # 對象名.wash() -> 就是用對象名.函數名來使用這個函數的功能

Samsung2 = Washer()     # 創建對象 # 對象名 = 類名()
Samsung2.wash()         # 對象名.wash() -> 就是用對象名.函數名來使用這個函數的功能
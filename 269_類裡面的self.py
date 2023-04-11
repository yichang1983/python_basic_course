# 類:洗衣機, 功能:洗衣服

class Washer():
    def wash(self):
        print('洗衣服')
        print(self)

Samsung = Washer()      # 創建對象 # 對象名 = 類名()
print(Samsung)
Samsung.wash()          # 對象名.wash() -> 就是用對象名.函數名來使用這個函數的功能



# 由於打印對象和打印self得到的內存地址相同.所以self指的是調用該函數的對象
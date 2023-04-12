class Washer():
    def wash(self):
        print('洗衣服')

    # 獲取對象屬性
    def print_info(self):
        print(self.width)       # 400
        print(f'洗衣機的寬度是{self.width}')
        print(f'洗衣機的高度是{self.height}')

Samsung = Washer()

#添加屬性 對象名.屬性名 ＝ 值
Samsung.width = 400
Samsung.height = 500

#對象調用方法
Samsung.print_info()
#目標：1. 定義類：帶參數的 init： 寬度和高度。 2. 實例方法：調用實例屬性
class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
        print(f'洗衣機的寬度是{self.width}, 高度是{self.height}')

Samsung1 = Washer(10, 20)   # 把 10 和 20 帶入到第3行的 width & height
Samsung1.print_info()       # 洗衣機的寬度是10, 高度是20

Samsung2 = Washer(200, 400) # 把 200 和 400 帶入到第3行的 width & height
Samsung2.print_info()       #洗衣機的寬度是200, 高度是400

#目標： 定義 init 魔法方法設置初始化屬性並訪問調用
""""
1。定義類
    init 魔法方法： width 和 height
    添加實例方法： 訪問實例屬性
2。創建對象
3。驗證成果
    調用實例方法
"""

class Washer():
    def __init__(self):
        #添加實例屬性
        self.width = 500
        self.height = 800

    def print_info(self):
        print(f'洗衣機的寬度是{self.width}')
        print(f'洗衣機的高度是{self.height}')

Samsung = Washer()

Samsung.print_info()

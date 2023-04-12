class Washer():
    def wash(self):
        print('洗衣服')
Samsung = Washer()

#添加屬性 對象名.屬性名 ＝ 值
Samsung.width = 400
Samsung.height = 500

#獲取屬性 對象名.屬性名
print(f'洗衣機的寬度是{Samsung.width}')
print(f'洗衣機的高度是{Samsung.height}')

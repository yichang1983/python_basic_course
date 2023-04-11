# 需求: 洗衣機, 功能:能洗衣服
# 1. 定義洗衣機類
"""
class 類名():
    代碼
"""

class Washer():
    def wash(self):
        print ('能洗衣服')
# 2.創建對象
# 對象名 = 類名()
Samsung = Washer()

# 3. 驗証成果
# 打印Samsung 對象
print(Samsung)      # <__main__.Washer object at 0x000001BAB89C3240>

# 使用wash功能--實列方法/對象方法 -- 對象名.wash()
Samsung.wash()      # 能洗衣服
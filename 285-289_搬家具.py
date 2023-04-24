class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area

class Home():
    def __init__(self, address, area):
        # 地理位置
        self.address = address      # 添加對象屬性:類裡面(self.屬性名 = 值)
        # 房屋面積
        self.area = area            # 添加對象屬性:類裡面(self.屬性名 = 值)
        # 剩餘面積
        self.free_area = area       # 添加對象屬性:類裡面(self.屬性名 = 值)
        # 家具列表
        self.furniture = []
    def __str__(self):
        return f'location is {self.address}, House size is {self.area}, 剩餘面積: {self.free_area}, 家具有:{self.furniture} '

    def add_furniture(self, item):
        """容納家具"""
        # 如果家具佔地面積 <= 房子剩餘面積: 可以搬入(家具列表添加家具名字數據並房子剩餘面積更新:
        # 房屋剩餘面積-該家具的佔地面積
        # 否則:提示用戶家具太大,剩余面積不足,無法容納.
        if item.area <= self.free_area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print("家具太大,剩余面積不足,無法容納")


bed = Furniture('double bed', 100)      #創建對象( 對象名 = 類名() )
sofa = Furniture('sofa', 50)            #創建對象( 對象名 = 類名() )
stadium = Furniture('statdium', 1500)   #創建對象( 對象名 = 類名() )

real_home = Home('London', 1000)        #創建對象( 對象名 = 類名() )
print(real_home)
real_home.add_furniture(bed)
print(real_home)
real_home.add_furniture(sofa)
print(real_home)
real_home.add_furniture(stadium)
print(real_home)
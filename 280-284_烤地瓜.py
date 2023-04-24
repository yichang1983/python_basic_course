# 1.定義類:初始化屬性,被烤和添加調料的方法, 顥示對象信息的str
class SweetPotato():
    def __init__(self):
        # 被烤的時間
        self.cook_time = 0
        # 烤的狀態
        self.cook_state = '生的'
        # 調料列表
        self.condiments = []

    def cook(self, time):
        """烤地瓜方法"""
        # 1.先計算地瓜整體烤過的時間
        self.cook_time += time
        # 2.用整體烤過的時間再判斷地瓜的狀態
        if 0 <= self.cook_time < 3:
            # 生的
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            # 半生不熟
            self.cook_state = '半生不熟'
        elif 5 <= self.cook_time < 8:
            # 熟了
            self.cook_state = '熟了'
        elif self.cook_time >= 8:
            # 烤糊了
            self.cook_state = '烤糊了'
    def add_condiments(self, condiments):
        self.condiments.append(condiments)

    def __str__(self):
        return f'這個地瓜被烤過的時間是{self.cook_time},狀態是{self.cook_state},調料有:{self.condiments}'

# 2. 創建對象並調用對應的實例方法
Real_sweetpotato = SweetPotato()
print(Real_sweetpotato)

Real_sweetpotato.cook(4)    # 把實列加上第13行的cook 函數
Real_sweetpotato.add_condiments('cheese')
print(Real_sweetpotato)

Real_sweetpotato.cook(4)
Real_sweetpotato.add_condiments('pepper')
print(Real_sweetpotato)
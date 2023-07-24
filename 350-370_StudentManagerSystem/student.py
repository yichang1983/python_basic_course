# 需求:
# 1.學員信息包含:姓名,性別,手機
# 2.添加__str__ 魔法方法,方便查看學員對象信息

class Student(object):
    def __init__(self, name, gender, tel):
        #姓名,性別,手機
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.name},{self.gender},{self.tel}'
# aa = Student('aa','female', 111)
# print(aa)
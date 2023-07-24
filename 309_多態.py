# 需求:警務人員和警犬一起工作, 警犬分2種:追擊敵人和追查毒品, 擕帶不同的警犬,執行不同的工作.

# 1. 定義父類, 提供公共方法:警犬和人
class Dog(object):
    def work(self):
        pass
# 2. 定義子類, 子類重寫父類方法: 定義2個類表示不同的警犬
class Armydog(Dog):
    def work(self):
        print('attack')

class DrugDog(Dog):
    def work(self):
        print('sniffing drug')

# 定義人類
class Person(object):
    def walk_with_dog(self, dog):
        dog.work()
# 3. 創建對象, 調用不同的功能,傳入不同的對象, 觀察執行的結果
ad = Armydog()
dd = DrugDog()
xiaoming = Person()

xiaoming.walk_with_dog(ad)      # attack
xiaoming.walk_with_dog(dd)      # sniff drug
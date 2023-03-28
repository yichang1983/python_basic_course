"""
1.出拳
    玩家:手動輸入
    電腦:1.固定:剪刀: 2.隨機
2.判斷輸贏
    2.1 玩家贏
    2.2 平手
    2.3 電腦贏
"""
# 導入模塊
import random

player = int(input('請出拳: 0 --石頭, 1 --剪刀, 2 --布'))
computer = random.randint(0, 2)
print(f'computer 出:{computer}')

if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print("玩家贏")
elif player == computer:
    print("平手")
else:
    print("電腦贏")


# 需求: 運行後暫停2秒打印hello
"""
1.導入time 模塊或導入time 模塊的sleep 功能
2.調用功能
3.打印hello
"""
# 1.模塊別名
import time as tt
tt.sleep(2)
print('hello')

#2.功能別名
from time import sleep as sl
sl(2)
print('world')
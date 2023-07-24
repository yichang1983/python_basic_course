# 需求: math模塊下sqrt()開平方計算
"""
1.導入模塊
2.測試是否導入成功: 調用該模塊內的 sqrt 功能
"""
# 方法一: import 模塊名; 模塊名.功能
import math
print (math.sqrt(9))

# 方法二: from 模塊名 import 功能1, 功能2...; 功能調用（不需要寫模塊名.功能）
from math import sqrt
print(sqrt(4))

# 方法三: from 模塊名 import * ; 功能調用（不需要寫模塊名.功能）
from math import *
print(sqrt(16))

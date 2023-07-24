#1.導入管理系統模塊
from managerSystem import *

#啓動管理系統
# 保證是當前文件運行才啟動管理系統: if --創建對象並調用run 方法
if __name__ == '__main__':
    student_manager = StudentManager()
    student_manager.run()

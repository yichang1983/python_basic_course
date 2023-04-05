"""
1.導入模塊 os
2.使用模塊內功能
"""
import os
# 1. rename(): 重命名
# os.rename('test_backup.txt','5678.mp4')

# 2. remove(): 刪除文件
# os.remove('5678.mp4')

# 3. mkdir(): 創建文件夾
# os.mkdir('aa')

# 4. rmdir(): 刪除文件夾
# os.rmdir('aa')

# 5. getcwd(): 返回當前文件所在目錄路徑
# print(os.getcwd())      #C:\Users\sp005\Desktop\code

# 6. chdir(): 改變目錄路徑
# os.mkdir('aa')
# 需求:在aa裡面創建bb文件夾: 1.切換目錄到aa, 2.創建bb
# os.chdir('aa')
# os.mkdir('bb')

# 7. listdir(): 獲取芋個文件夾一所有文件,返回一個列表.
# print(os.listdir())     # ['.idea', '200_引用當做實參.py', '205_學員管理系統.py', '221_遞歸之回顧函數返回值.py', '222_遞歸的應用.py', '226_體驗lambda.py', '227_lambda加法計算.py', '228-232_lambda參數形式.py', '233_帶判斷的lambda.py', '234_列表數據的排序.py', '236_abs & round 的function.py', '238_體驗高階函數.py', '239_高階函數-map.py', '240_高階函數-reduce.py', '241_高階函數-filter.py', '244_體驗文件操作.py', '245_主訪問模式_w,r,a文件操作.py', '246_讀取函數之read.py', '247_讀取函數之readlines.py', '248_讀取函數之readline.py', '251_seek函數.py', '254-256_文件備份.py', '257_文件和文件夾操作.py', 'aa', 'bb', 'main.py', 'myFirstPython.py', 'Phtyon course', 'test.txt', 'test1.txt', 'test1_backup.txt']
# print(os.listdir('aa'))     # ['bb']

# 8. rename(): 重命名文件夾, 把bb 變成bbbb
os.rename('bb', 'bbbb')


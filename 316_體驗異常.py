#需求:嘗試打開test.txt (r), 如果文件不存在, 用寫的方式打開 (w)
"""
try:
    可能發生錯誤的代碼
except:
    發生錯誤的時候執行的代碼
"""

try:
    open("test.txt", "r")
except:
    open("test.txt", "w")


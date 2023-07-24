#需求:嘗試以r打開文件, 如果有異常以w打開這個文件, 最終關閉文件

try:
    f = open('test100.txt', 'r')
except Exception as e:
    f = open('test100.txt', 'w')
finally:
    f.close()


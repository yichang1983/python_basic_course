#需求:嘗試只讀打開test.txt 文件存在讀取內容,不存在提示用戶
#需求2: 讀取內容:循環讀取,當無內容的時候退出循環,如果用戶意外止,提示用戶己經被意外終止
import time

try:
    f = open('test.txt')
    #嘗試循環讀取內容
    try:
        while True:
            con = f.readline()
            if len(con) == 0:
                #如果讀取完成退出循環
                break
            time.sleep(3)
            print(con)
    except:
        #在命令提示符中如果按下Ctrl + C 結束終止的鍵
        print('the program has been terminated')

except:
    print('the file does not exist')

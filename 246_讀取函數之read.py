# 文件內容如果換行,底層有\n. 會有字節佔位,導玫read書寫參數取出來的眼睛看到的個數和參數值不匹配.
# read 不寫參數表示讀取所有.

f = open('test.txt', 'r')
# print(f.read())   # 印出所有的文字
print(f.read(10))   # "aaaaa bbbb" -> 印出10個字節的文字.
f.close()

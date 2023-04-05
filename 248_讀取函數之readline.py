# readline： 一次執行只讀取一行。
f = open('test.txt')
content = f.readline()
print(f'第一行是: {content}')  # 第一行是: aaaaa

content = f.readline()
print(f'第二行是: {content}')   # 第二行是: bbbbb

content = f.readline()
print(f'第二行是: {content}')   #　第二行是: ccccc
f.close()

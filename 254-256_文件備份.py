# 1.用戶輸入目標文件:  sound.txt.mp3
old_name = input('請輸入您要備份的文件名: ')
# print(old_name)
# print(type(old_name))

# 2.規劃備份文件的名字
# 2.1.提取後綴 -- 找到名字中的點 -- 名字和後綴分離--最右側的點才是後綴的點--字符串查找业個子串 rfind.
index = old_name.rfind('.')             # 用rfind 去從後面找尋 '.'
print(index)

# 4.思考:有效文件才備份  '.txt'(就不行)
if index > 0:
    postfix = old_name[index:]

# 2.2. 組織新名字 = 原名字 + _backup + 後綴
# 原名字就是字符串中的一部份子串 -- 切片[開始:結束:步長]
print(f'前綴是:{old_name[:index]}')        # 前綴是:sound.txt -> 前綴是用 '.' 之前的文字
print(f'後綴是{old_name[index:]}')         # 後綴是.mp3       -> 後綴是用 '.' 之後的文字

# new_name = old_name[:index] + '_backup' + old_name[index:]
new_name = old_name[:index] + '_backup' + postfix
print(new_name)                            # sound.txt_backup.mp3

# 3.備份文件寫入數據(數據和原文件一樣)
# 3.1 打開原文件和備份文件
old_file = open(old_name, 'rb')         # rb 中的b 是指二進制
new_file = open(new_name, 'wb')         # wb 中的b 是指二進制

# 3.2 原文件讀取, 備份文件寫入
# 如果不確定目標文件大小,循環讀取寫入, 當讀取出來的數據沒有了終止循環.
while True:
    content = old_file.read()
    if len(content) == 0:
        break
    new_file.write(content)

# 3.3 關閉文件
old_file.close()
new_file.close()
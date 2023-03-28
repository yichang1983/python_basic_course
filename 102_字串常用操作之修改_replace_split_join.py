mystr = "hello world and itcast and itheima and Python"

#1. replace() 把 and 換成 or  #說明 replace 函數有返回值，返回值是修改後的字符串
# newm_ystr= mystr.replace('and','or')        # hello world or itcast or itheima or Python
# newm_ystr= mystr.replace('and','or', 1)     # hello world or itcast and itheima and Python
# 替換次數如果超出子串出現的次數，表示替換所有這個子串
# newm_ystr= mystr.replace('and','or', 1)
# print(newm_ystr)

# 2. split() -- 分割，返回一個列表，丟失分割
# new_str1 = mystr.split("and")       #['hello world ', ' itcast ', ' itheima ', ' Python']
# new_str1 = mystr.split("and", 2)  # ['hello world ', ' itcast ', ' itheima and Python']
# print(new_str1)

# 3. join() -- 合併列表裡面的字符串數據為一個大字符串
str2 = ['aa','bb','cc']

# aa...bb...cc
new_str2 = '...'.join(str2)         #aa...bb...cc
print(new_str2)


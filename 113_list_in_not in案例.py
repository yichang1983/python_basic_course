my_list = ['Tom','Lily','John']

# 需求:注冊郵箱, 用戶輸入一個帳號名, 判斷這個帳號是否存在, 如果存在,提示用戶, 否則提示可以注冊
"""
1.用戶輸入帳號
2.判斷if...else
"""

name = input("請輸入你的郵箱帳號: ")
if name in my_list:
    print("此名稱己經有了,輸入別的")
else:
    print("可以用此名稱")

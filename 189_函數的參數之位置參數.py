# 需求：函數3個參數 name, age, gender

def user_info(name, age, gender):
    print(f'你的姓名是{name}, 年紀是{age}, 性別是{gender}')

# user_info('Tom', 30, '男')        # 你的姓名是Tom, 年紀是30, 性別是男
# user_info('Tom', 30, )          # 個數定義和傳入不一致會報錯
user_info(20,'Tom','男')         #你的姓名是20, 年紀是Tom, 性別是男 ，順序不一致導致結果是無意義。

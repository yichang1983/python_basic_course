def user_info(name, age, gender='男'):
    print(f'你的姓名是{name}, 年紀是{age}, 性別是{gender}')

user_info('Tom', 30)         # 你的姓名是Tom, 年紀是30, 性別是男        沒有為缺省參數傳值，表示使用默認值
user_info('Rose', 52,'女')   # 你的姓名是Rose, 年紀是52, 性別是女        為缺省參數傳值，使用這個值，即修改了默認值
user_info('Rose', 52, gender='女')   # 你的姓名是Rose, 年紀是52, 性別是女
user_info(age=30, name='Liam' )      # 你的姓名是Liam, 年紀是30, 性別是男   順序也可以不一樣，只要書寫age, name 來相對應即可。





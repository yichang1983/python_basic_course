def user_info(name, age, gender):
    print(f'你的姓名是{name}, 年紀是{age}, 性別是{gender}')

# 調用函數傳參
user_info('ROSE', age=30, gender='female')
user_info('Tom', gender='male', age=30)         # 關鍵字參數之間不分先後順序
user_info(age=50, gender='male',name='John')

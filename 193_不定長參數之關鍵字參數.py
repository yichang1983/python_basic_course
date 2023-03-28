# 收集所有關鍵字參數，返回一個字典
def user_info(**kwargs):
    print(kwargs)

user_info()     # {}
# user_info('Tom')        # TypeError: user_info() takes 0 positional arguments but 1 was given
user_info(name='Tom')     # {'name': 'Tom'}
user_info(name='Nancy', age=50)     # {'name': 'Nancy', 'age': 50}

"""
總結：user_info(**kwargs) 在 **kwagus 裡不管傳入多少都會被接收,但必需是關鍵字參數（key=value），之後它會返回一個字典的形式。
"""

#以下是自己去測試
def user_info1(**kwargs):
    print(f'你的姓名是{kwargs}, 性別是{kwargs}')

user_info1(name='John', gender='male')  # 你的姓名是{'name': 'John', 'gender': 'male'}, 性別是{'name': 'John', 'gender': 'male'}

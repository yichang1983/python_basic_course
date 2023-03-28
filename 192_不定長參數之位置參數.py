# 接收所有位置參數，返回一個元組
def user_info(*args):
    print(args)

user_info('Tom')                            # ('Tom',)
user_info('Tom', 50)                        # ('Tom', 50)
user_info('Tom', 50,'male', 'non smoking')  # ('Tom', 50, 'male', 'non smoking')
user_info()                                 # ()

"""
總結：user_info(*args) 在 *agus 裡不管傳入多少都會被接收
"""


#以下是自己去測試
def user_info1(*args):
    print(f'你的姓名是{args}, 年紀是{args},性別是{args}')

user_info1(20,'John','male') # 你的姓名是(20, 'John', 'male'), 年紀是(20, 'John', 'male'),性別是(20, 'John', 'male')

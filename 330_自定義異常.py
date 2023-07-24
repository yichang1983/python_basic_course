#1.自定義異常類,繼承Exception. 魔法方法有init 和str(設置異常描述信息)
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        # 用戶輸入的密碼長度
        self.length = length
        # 系統要求的最少長度
        self.min_len = min_len
    # 設置異常描述信息
    def __str__(self):
        return f'您輸入的密碼長度是{self.length},密碼不能少於{self.min_len}'

def main():
    # 2. 拋出異常:嘗試執行:用戶輸入密碼,如果長度小於3, 拋出異常
    try:
        password = input('請輸入密碼: ')
        if len(password) < 3:
            raise ShortInputError(len(password), 3)
    # 3.捕獲該異常
    except Exception as result:
        print(result)
    else:
        print('沒有異常,密碼輸入完成')
main()
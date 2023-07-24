#else 表示的是如果沒有異常要執行的代碼

try:
    print(1)
except Exception as result:
    print(result)
else:
    print('我是else,當沒有異常的時候執行的代碼')

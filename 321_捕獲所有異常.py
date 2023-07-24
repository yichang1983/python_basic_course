#嘗試執行打印 num, 捕獲 Exception 打印異常描述訊息, Exception 是所有異常的父類.

try:
    print(num)
except Exception as result:
    print(result)

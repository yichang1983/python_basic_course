#需求:嘗試執行打印 num, 捕獲異常類型NameError, 如果捕獲到這個異常類型, 執行打印:有錯誤


try:
    print(num)
except NameError:
    print("有錯誤")


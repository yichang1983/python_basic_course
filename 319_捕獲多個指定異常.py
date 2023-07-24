try:
    print(1/0)
except (NameError, ZeroDivisionError):      # 指定多個錯誤,當其中之一有捕獲到,則執行下方的程式碼
    print("有錯誤")

# 1. 使用一個函數
# 2. 測試注意事項
# 3. 需求： 一個函數： 打印 hello world


# info_print()    # 報錯

# 定義函數

def info_print():
    print("hello world")

# 調用函數
info_print()


""" 
結論：
1。 函數先定義後調用，如果先調用會報錯
2。 如果沒有調用函數，函數裡面的代碼不會執行
3。 函數執行流程 ***
    當調用函數的時候，解釋器回到定義函數的地方去執行下方縮進的代碼，當這些代碼執行完，回到調用函數的地方繼續向下執行。

"""
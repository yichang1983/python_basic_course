# 1。打印多條橫線圖形

def print_line():
    print('-'  * 20)

# print_line()

def print_lines(num):           # num 只是一個形參, 可以把它想成變數參數，它是要給第 14行中的 print_lines() 括狐中來做使用。
    i = 0
    while i < num:              # 當第14號中的 print_lines() 括狐 數字是多少，num 就是等於此數字。
        print_line()            # 使用上方定義的 print_line 函數。
        i += 1

print_lines(5)                  # 3 （數字）是一個實參， 表示代入 第八行的num（形參）。


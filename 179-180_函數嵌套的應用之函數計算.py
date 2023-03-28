# 1。任意三個數之和
def sum_num(a,b,c):
    return a+b+c

result = sum_num(1,2,3)         # sum_num(1+2+3) 就是 return 結果的返回值，然而再用 result 去把它存下來。
# print(result)                   # 6


# 2。任意三個數求平均數
def average_sum(a,b,c):             # a=1,b=2,c=3 從第十四行得到，如果在行參打入average_sum(d,e,f),則第11行就會出錯。
    sum_result = sum_num(a,b,c)     # a=1,b=2,c=3
    return sum_result / 3

ave_result = average_sum(1,2,3)
print(ave_result)


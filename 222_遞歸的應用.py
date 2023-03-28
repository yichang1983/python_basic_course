# 需求： 3以內數字累加和 3 + 2 + 1 ＝ 6
# 6 ＝ 3 ＋ 2 以內數字累加和
# 2以內數字累加和 ＝ 2 + 1 以內數字累加和
# 1以內數字累加和 ＝ 1  # 出口

# 遞歸特點： 函數內部自己調用自己； 必需有出口

def sum_numbers(num):
    # 2。出口
    if num == 1:
        return 1
    # 1。當前數字 ＋ 當前數字-1的累加和（sum_numbers(num-1) --> 函數內部自己調用自己）
    return num + sum_numbers(num-1)

result = sum_numbers(5)
print(result)



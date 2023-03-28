# 坐公車:如果有錢可以上車, 沒錢不能上車, 如果上車了,判斷能否坐下 -- 是否有空座位

"""
步驟:
    1. 準備將來要做判斷的數據: 錢和空座
    2. 判斷是否有錢: 上車 和 不能上車
    3. 上車了: 判斷是否能坐下: 有空座位 和無空座位
"""
money = 1
seat = 0

if money == 1:
    print("you have money")
    # 判斷是否有座位
    if seat == 1:
        print("seat is available")
    else:
        print("seats are occupied")
else:
    print("you don't have money")



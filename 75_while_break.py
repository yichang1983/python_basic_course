# break:當某些條件成立, 退出整個循環
#循環吃5個蘋果, 吃完第三個吃飽了, 第4,5個不吃了 == 4,或 >3

i = 1
while i <= 5:
    if i > 3:
        print("I am full")
        break
    print(f"吃了第{i}個蘋果")
    i += 1

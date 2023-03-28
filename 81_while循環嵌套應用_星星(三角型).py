# j 表示行號
j =1
while j < 6:
    i = 1
    # i表示每行裡面星星的個數, 這個數字要和行號相等所以i要和j聯動
    while i <= j:
        print("*", end="")
        i += 1
    print()
    j += 1


# 1。聲明全局變量。 2。定義二個函數。 3。函數一修改全局變量：函數2訪問全局變量
glo_num = 0

def test1():
    global glo_num
    glo_num = 100

def test2():
    print(glo_num)

print(glo_num)      # 0, 因為倐改的函數沒執行。
test2()             # 0，因為修改的函數沒執行。
test1()
test2()             # 100，因為先調用了test1函數
print(glo_num)      # 100，因為調用了test1函數

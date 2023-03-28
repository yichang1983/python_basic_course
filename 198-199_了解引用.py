# 可變和不可變
#1。不可變：int: 1.1聲明變量保存整型數據。把這個數據賦值到另一個變量：id()檢測二個變量的id值（內存的十進制）
a = 1
b = a
print(b)        # 1

# 發現a and b 的 id 值相同
print(id(a))        # 4373095592
print(id(b))        # 4373095592

# 修改a的數據測試 id 值
a = 2

print(b)        # 1

#因為修改了a的數據，內存要開闢另外一份內存儲存2，id檢測a and b 的地址不同。
print(id(a))    # 4385400008
print(id(b))    # 4385399976

# 2。 可變類型：列表
aa = [10, 20]
bb = aa
print(aa)       # [10, 20]
print(bb)       # [10, 20]
print(id(aa))   # 4301326336
print(id(bb))   # 4301326336

aa.append(30)
print(aa)       # [10, 20, 30]
print(bb)       # [10, 20, 30]      當可變類型改變數據，b的值也會改變，但內存的id 還是一樣。
print(id(aa))   # 4301326336
print(id(bb))   # 4301326336


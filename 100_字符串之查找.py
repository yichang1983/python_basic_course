mystr = "hello world and this and test and python"

# 1.find()
# print(mystr.find("and")) #12
# print(mystr.find("and",15,30)) #21
print(mystr.find("anndgs"))  #-1 (子串不存在)

# 2.index()
# print(mystr.index("and")) #12
# print(mystr.index("and",15,30)) #21
# print(mystr.index("ands")) #ands 子串不存在,報錯

# 3.count()
# print(mystr.count("and"))  # 3
# print(mystr.count("and",15,30)) #1
# print(mystr.count("ands")) #0

# 4.rfind()
# print(mystr.rfind("and")) #30
# print(mystr.rfind("ands")) #-1

# 5.rindex()
# print(mystr.rindex("and")) #30
# print(mystr.rindex("ands")) #子串不存在,報錯
# 需求1: 把bb文件夾所有文件重命名外Python_xxx
import os
# 1.找到bb文件夾:獲取目錄列表-listdir()
folder_name = os.listdir('../bb')
print(folder_name)
# 構造條件的數據
flag = 2
# 2.構造名字
for i in folder_name:
    if flag == 1:
        new_name = 'Python_' + i
        original_path = os.path.join('../bb', i)
        new_path = os.path.join('../bb', new_name)
    elif flag == 2:
        num = len('Python_')
        new_name = i[num:]
        original_path = os.path.join('../bb', i)
        new_path = os.path.join('../bb', new_name)
# 3.重新命名
    os.rename(original_path, new_path)

#
# import os
#
# # 1. Find the "bb" folder: get directory list using listdir()
# folder_name = os.listdir('bb')
# print(folder_name)
#
# # 2. Construct new names for each file in the folder
# for i in folder_name:
#     # Construct new name by adding "Python_" prefix to original filename
#     new_name = 'Python_' + i
#
#     # Get full path to the file by joining the "bb" folder path with the original filename
#     original_path = os.path.join('bb', i)
#     new_path = os.path.join('bb', new_name)
#
#     # 3. Rename the file using the new name
#     os.rename(original_path, new_path)

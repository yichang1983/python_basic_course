#需求: 8位老師, 3個辦公室. 將8位老師隨機分配到3個辦公室

"""
步驟:
1.準備數據:
    1.1 8位老師 --列表
    1.2 3個辦公室 - 列表嵌套
2. 分配老師到辦公室
    ***隨機分配
    就是把老師的名字寫入到辦公室列表 -- 辦公室列表追加老師名字數據
3. 驗證是否分配成功
    打印辦公室詳細信息: 每個辦公室的人數和對的的老師名字
"""
import random
# 1.準備數據:
teachers = ['Tom','John','Nancy','Chad', 'Chen', 'K', 'Bob', 'Apple']
offices = [[], [], []]

# 2.分配老師到辦公室
for teacher in teachers:
    # 列表追加數據, -- append(), extend, insert
    # xx[0] -- 不能指定是具體芋個下標 --隨機
    num = random.randint(0, 2)
    offices[num].append(teacher)
print(offices)

# 3.驗證是否分配成功
# 為了更貼合生活, 把各個辦公室子列表加一個辦公室編號1,2,3
i = 1
for office in offices:
    print(f'辦公室{i}的人數是:{len(office)}, 老師的名字分別是:')
    # 打印老師的名字
    # print() -- 個個子列表裡面的名字個數不一定 -- 遍历  -- 子列表
    for teacher_num in office:
        print(teacher_num)
    i += 1

















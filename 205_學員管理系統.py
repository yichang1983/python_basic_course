#  定義功能界面函數:
def info_print():
    print('請選擇功能------------')
    print('1.添加學員')
    print('2.刪除學員')
    print('3.修改學員')
    print('4.查詢學員')
    print('5.顯示所有學員')
    print('6.退出系統')
    print('-' * 20)

# 等待儲存所有學員的訊息
info = []

# 1.添加學員訊息的函數
def add_info():
    """添加學員函數"""
    # 1.用戶輸入:姓名,年齡,手機
    new_name = input("請輸入姓名")
    new_age = input("請輸入年齡")
    new_tel = input("請輸入手機")
    # 2. 判斷是否添加這個學員,如果學員的姓名己經存在, 提示報錯; 如果姓名不存在添加數據
    global info
    # 2.1 不允許姓名重覆:判斷用戶輸入的姓名和列表裡面字典的name對應的值相等提示
    for i in info:
        if new_name == i['name']:
            print('姓名重覆')
            # return 作用:退出當前函數,後面淚加訊息的代碼不執行
            return

    # 2.2 如果輸入的姓名不存在, 添加數據:準備空字典,字典新增數據,列表追加字典.
    info_dict = {}
    info_dict['name'] = new_name
    info_dict['age'] = new_age
    info_dict['tel'] = new_tel
    # print(info_dict)
    info.append(info_dict)
    print(info)

# 2.刪除學員的函數
def del_info():
    """刪除學員"""
    # 1.用戶輸入要刪除學員的姓名.
    del_name = input('請輸入要刪除的學員姓名: ')
    # 2. 判斷學員是否存在: 存在則刪除;不存在則提示"不存在"
    # 2.1 聲明 info 是全局變量
    global info
    # 2.2 遍歷列表
    for j in info:
        if del_name == j['name']:
    # 2.3 判斷學員是否存在, 存在執行刪除(列表裡的字典). break:這個系統不允許重覆名字,刪除了一個後面的不需要再遍歷.
            info.remove(j)
            break

    else:                               # 這兒的else 是指當 for 循環正常結束時,要做以下的事.
        print('要刪除的學員姓名不存在')
    print(info)

# 3.修改學員的函數
def modify_info():
    """修改學員的函數"""
    # 1.用戶輸入想要修改學員的姓名
    modify_name = input('輸入想要修改學員的姓名')
    # 2.判斷學員是否存在,存在時修改手機號, 不存在時, 顯示該學員不存在.
    # 2.1 聲明info 是全局
    global info
    # 2.2 遍歷列表,判斷輸入的姓名 == 字典['name']
    for z in info:
        if modify_name == z['name']:
            z['tel'] = input('請輸入您要更改的手機號碼: ')        # 將要更改的手機存到 tel 裡.
            break
    # 2.3. 顯示該學員不存在
    else:                       # 這兒的 else 是指"當遍歷正常完成後,要顯示的東西"
        print('該學員不存在.')
    # 3. 印列 info
    print(info)

# 4.查詢學員訊息的函數
def search_info():
    """查詢學員訊息"""
    # 1.用戶輸入要查詢的學員
    search_name = input('輸入要查詢的學員:')
    # 2.檢查學員是否存在,存在時印出這個學員的資訊;不存在時顯示沒有該名學員.
    # 2.1 聲明 global
    global info
    # 2.2 遍歷info, 判斷輸入的學員是否存在
    for i in info:
        if search_name == i['name']:
            print('此學員的資訊如下:----------')
            print(f"姓名是{i['name']},年紀是{i['age']},電話是{i['tel']}")
            break
    # 2.3 不存在時顯示沒有該名學員
    else:
        print('沒有該名學員')

# 5.顯示所有學員訊息的函數
def all_info():
    """顯示所有學員訊息"""
    # 1. 打印提示字
    print('姓名\t年紀\t電話\t')           #\t 是指讓它對齊
    # 2. 打印所有學員的資訊
    for i in info:
        print(f"{i['name']}\t{i['age']}\t{i['tel']}\t")     #\t 是指讓它對齊

# 系統功能循環使用,直到用戶輸入6 退出系統
while True:
    # 1.顯示功能介面
    info_print()

    # 2.用戶輸入功能序號
    user_num = int(input('請輸入功能序號: '))

    # 3.按照用戶輸入的功能序號, 執行不同的功能(函數)
    # 如果用戶輸入1. 執行添加; 如果用戶輸入2. 執行刪除... --多重判斷

    if user_num == 1:
        add_info()
        # print("添加學員")
    elif user_num == 2:
        del_info()
        # print("刪除學員")
    elif user_num == 3:
        modify_info()
        # print("修改學員")
    elif user_num == 4:
        search_info()
        # print("查詢學員")
    elif user_num == 5:
        all_info()
        # print("顯示所有學員")
    elif user_num == 6:
        # 程式想要結束, 退出終止 while True -- break
        exit_flag = input('確定要退出系統? YES OR NO:')
        if exit_flag == 'YES':
            break
    else:
        print("輸入序號有誤")

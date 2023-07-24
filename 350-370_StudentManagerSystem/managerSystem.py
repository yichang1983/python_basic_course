from student import *

class StudentManager(object):
    def __init__(self):
        # 存儲數據所用的列表
        self.student_list = []
    # 一.程序入口函數
    def run(self):
        #1.加載文件裡面的學員數據
        self.load_student()
        while True:
            # 2.顯示功能菜單
            self.show_menu()    #調用show_menu,因為它在class 的類裡,如需調用,需要用self.函數(self.show_menu)去調用
            # 3.用戶輸入目標功能序號
            menu_num = int(input('請輸入您需要的功能序號:'))
            # 4.根據用戶輸入的序號執行不同的功能--如果用戶輸入1.添加,2.刪除..等
            if menu_num == 1:
                #添加學員
                self.add_student()
            elif menu_num == 2:
                # 刪除學員
                self.del_student()
            elif menu_num == 3:
                # 修改學員
                self.modify_student()
            elif menu_num == 4:
                # 查詢學員
                self.search_student()
            elif menu_num == 5:
                # 顯示所有學員訊息
                self.show_student()
            elif menu_num == 6:
                # 保存學員訊息
                self.save_student()
            elif menu_num == 7:
                # 退出系統 -- 退出循環
                break

    # 二.系統功能函數
    #2.1 顯示功能菜單 -- 打印序號的功能對應關係 --靜態
    @staticmethod
    def show_menu():
        print('請選擇如下功能')
        print('1.添加學員')
        print('2.刪除學員')
        print('3.修改學員')
        print('4.查詢學員訊息')
        print('5.顯示所有學員訊息')
        print('6.保存學員訊息')
        print('7.退出系統')
    #2.2 添加學員
    def add_student(self):
        #1.用戶輸入姓名,性別手機號
        name = input('請輸入您的姓名')
        gender = input('請輸入您的性別')
        tel = input('請輸入您的手機號')
        #2.創建學員對象 --類? 類在student文件裡, 先導入模塊,再創建對象
        student = Student(name, gender, tel)

        #3.將該對象添加到學員列表
        self.student_list.append(student)
        print(self.student_list)
        print(student)
    #2.3 刪除學員
    def del_student(self):
        #1.用戶輸入目標學員姓名
        del_name = input('請輸入要刪除的學員姓名: ')

        #2.遍歷學員列表,如困用戶輸入的學員存在則刪除學員對象,否則提示學員不存在
        for i in self.student_list:
            if del_name == i.name:      #i是變數, 也就是每次找尋self.student_list 存成i, i.name 也就是self.student_list 中的 name值
                #刪除該學員對象
                self.student_list.remove(i)
                break
        else:
            #循環正常結束執行的代碼:循環結束都沒有刪除任何一個對象,所以哾明用戶輸入的目標學員不存在.
            print('查無此人')

        print(self.student_list)

    #2.4 修改學員
    def modify_student(self):
        #1.用戶輸入目標學員姓名
        modify_name = input('請輸入要修改的學員姓名: ')
        #2.遍歷學員列表,如學員存在則修改學員姓名,性別及手機號,否則提示學員不存在
        for i in self.student_list:
            if modify_name == i.name:
                i.name = input('姓名: ')
                i.gender = input('性別: ')
                i.tel = input('手機號: ')
                print(f'修改學員訊息成功, 姓名{i.name}, 性別{i.gender},手機號{i.tel}')
                break
            else:
                print('查無此人')

    #2.5 查詢學員訊息
    def search_student(self):
        #1.用戶輸入目標學員姓名
        search_name = input('請輸入要查詢的學員姓名: ')

        #2.遍歷學員列表,如學員存在則打印學員姓名,性別及手機號,否則提示學員不存在
        for i in self.student_list:
            if search_name == i.name:
                print(f'姓名:{i.name}, 性別:{i.gender},手機號:{i.tel}')
                break
        else:
            print('查無此人')

    #2.6 顯示所有學員訊息
    def show_student(self):
        #1.打印表頭
        print('姓名\t性別\t手機號')
        #2.打印學員數據
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')

    #2.7 保存學員訊息
    def save_student(self):
        #1.打開文件
        f = open('student.data', 'w')

        #2.文件寫入數據

        #2.1 [學員對象] 轉換成 [字典]: 文件寫入的數據不能是學員對象的內存地址, 需要把學員數據轉換成列表字典數據再做存儲
        new_list = [i.__dict__ for i in self.student_list]

        #2.2 文件寫入 字符串數據: 文件內數據要求為字符串類型,故需要先轉換數據類型為字符串才脦文件寫入數據
        f.write(str(new_list))

        #.關閉文件
        f.close()
    #2.8 加載學員訊息
    def load_student(self):
        #1. 打開文件:嘗試r打開, 如果有異常,用w 打開
        try:
            f = open('student.data','r')
        except:
            f = open('student.data', 'w')
        else:
        #2. 讀取數據:文件讀取出的數據是字串,還原列表類型:[{}] 轉換 [學員對象]
            data = f.read()     #data 讀出來就是字串
            new_list = eval(data)
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
        finally:
    # 3. 關閉文件
            f.close()



# 需求:
# 1.存儲數據的位置:文件(student.data)
# -加載文件數據
# -修改數據後保存到文件
# 2.存儲數據的形式:列表存儲學員對象
# 3.系統功能
# -添加學員
# -刪除學員
# -修改學員
# -查詣學員學員
# -顯示所有學員信息
# -保存學員信息
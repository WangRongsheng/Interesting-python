import time

def meun():
    menu_info = '''＋－－－－－－－－－－－－－－－－－－－－－－＋
｜ １）添加学生信息                           ｜
｜ ２）显示所有学生的信息                     ｜
｜ ３）删除学生信息                           ｜
｜ ４）修改学生信息                           ｜
｜ ５）按学生外出次数高－低显示学生信息       ｜
｜ ６）按学生外出次数低－高显示学生信息       ｜
｜ ７）按学生所在地确诊人数高－低显示学生信息 ｜
｜ ８）按学生所在地确诊人数低－高显示学生信息 ｜
｜ ９）保存学生信息到文件（students.txt)      ｜
｜ １０）从文件中读取数据（students.txt)      ｜
｜ 退出：其他任意按键＜回车＞                 ｜
＋－－－－－－－－－－－－－－－－－－－－－－＋
'''
    print(menu_info)

def get_outgotimes(*a):
    for i in a:
        return i.get("outgotimes")
def get_people(*a):
    for i in a:
        return i.get("people")
# 1)添加学生信息
def add_student_info():
    L = []
    while True:
        sid = input("请输入学号:")
        if not sid: #学号为空跳出循环
            break
        n = input("请输入姓名:")
        if not n: #名字为空，跳出循环
            break
        try:
            a = int(input("请输入外出次数:"))
            s = int(input("请输入所在地确诊人数:"))
        except:
            print("输入无效，请输入整数....重新录入信息")
            continue
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        info = {"id":sid,"name":n,"outgotimes":a,"people":s,"intimes":t}
        L.append(info)
    print("学生信息录入完毕！！！")
    return L

# 2)显示所有学生的信息
def show_student_info(student_info):
    if not student_info:
        print("无数据信息......")
        return
    print("学号".center(12),"姓名".center(8),"外出次数".center(8),"确诊人数".center(8),"录入时间".center(30))
    for info in student_info:
        print(info.get("id").center(12),info.get("name").center(8),str(info.get("outgotimes")).center(8),str(info.get("people")).center(8),info.get("intimes").center(30))

# 3) 删除学生信息
def del_student_info(student_info,del_name = ''):
    if not del_name:
        del_name = input("请输入删除的学生姓名：")
    for info in student_info:
        if del_name == info.get("name"):
            print("学生信息即将被删除或更新")
            return info
    raise IndexError("学生信息不匹配,没有找到%s" %del_name)

# 4) 修改学生信息
def mod_student_info(student_info):
    mod_name = input("请输入修改的学生姓名:")
    for info in student_info:
        if mod_name == info.get("name"):
            m = input("请输入学号:")
            if not m:
                break
            a = int(input("请输入外出次数:"))
            s = int(input("请输入所在地确诊人数:"))
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            info = {"id":m,"name":mod_name,"outgotimes":a,"people":s,"intimes":t}
            return info
    raise IndexError("学生信息不匹配，没有找到%s"%mod_name)

# 5) 按学生外出次数高—低显示学生信息
def outgotimes_reduce(student_info):
    print("按学生外出次数高—低显示:")
    mit = sorted(student_info,key = get_outgotimes,reverse = True)
    show_student_info(mit)

# 6) 按学生外出次数低—高显示学生信息
def outgotimes_rise(student_info):
    print("按学生外出次数低—高显示:")
    mit = sorted(student_info,key = get_outgotimes)
    show_student_info(mit)

# 7) 按照学生所在地确诊人数高—低显示学生信息
def people_reduce(student_info):   
    print("按学生所在地确诊人数高－低显示学生信息：")
    mit = sorted(student_info ,key = get_people,reverse = True)
    show_student_info(mit)

# ８）按学生所在地确诊人数低—高显示学生信息
def people_rise(student_info): 
    print("按学生所在地确诊人数低—高显示学生信息")
    mit = sorted(student_info ,key = get_people)
    show_student_info(mit)

# ９）保存学生信息到文件（students.txt)
def save_info(student_info):
    try:
        students_txt = open("students.txt","w")     # 以写模式打开，并清空文件内容
    except Exception as e:
        students_txt = open("students.txt", "x")    # 文件不存在，创建文件并打开
    for info in student_info:
        students_txt.write(str(info)+"\n")          # 按行存储，添加换行符
    students_txt.close()

# １０）从文件中读取数据（students.txt) 
def read_info():
    old_info = []
    try:
        students_txt = open("students.txt")
    except:
        print("暂未保存数据信息")                       # 打开失败，文件不存在说明没有数据保存
        return
    while True:
        info = students_txt.readline()
        if not info:
            break
        #print(info)
        info = info.rstrip()    #　去掉换行符
        # print(info)
        info = info[1:-1]       # 去掉｛｝
        # print(info)
        student_dict = {}       # 单个学生字典信息
        for x in info.split(","):   # 以，为间隔拆分
            # print(x)
            key_value = []      # 开辟空间，key_value[0]存key,key_value[0]存value
            for k in x.split(":"):  # 以：为间隔拆分
                k = k.strip()       #　去掉首尾空字符
                # print(k)
                if k[0] == k[-1] and len(k) > 2:        # 判断是字符串还是整数
                    key_value.append(k[1:-1])           # 去掉　首尾的＇
                else:
                    key_value.append(str(k))
                # print(key_value)
            student_dict[key_value[0]] = key_value[1]   # 学生信息添加
        # print(student_dict)
        old_info.append(student_dict)   # 所有学生信息汇总
    students_txt.close()  
    return old_info   

    
def main():
    student_info = []
    while True:
        # print(student_info)
        meun()
        number = input("请输入选项：")
        if number == '1':
            student_info = add_student_info()
        elif number == '2':
            show_student_info(student_info)
        elif number == '3':
            try:
                student_info.remove(del_student_info(student_info))
            except Exception as e:
                # 学生学号不匹配
                print(e)            
        elif number == '4':
            try:                
                student = mod_student_info(student_info)
            except Exception as e:
                # 学生学号不匹配
                print(e)
            else:
                # 首先按照根据输入信息的名字，从列表中删除该生信息，然后重新添加该学生最新信息
                student_info.remove(del_student_info(student_info,del_name = student.get("name")))  
                student_info.append(student)
        elif number == '5':
            outgotimes_reduce(student_info)
        elif number == '6':
            outgotimes_rise(student_info)
        elif number == '7':
            people_reduce(student_info)
        elif number == '8':
            people_rise(student_info)
        elif number == '9':
            save_info(student_info)
        elif number == '10':
            student_info = read_info()
        else:
            break
        input("回车显示菜单")

main()

from gro import gro
import pickle as pk


def main():
    def printMenu():
        print("=" * 30)
        print("      学生管理系统")  # class maked
        print("1.添加学生信息")
        print("2.删除学生信息")
        print("3.修改学生信息")
        print("4.查询学生信息")
        print("5.显示所有学生信息")
        print("6.导出外部文件")
        #print("7.导入外部文件")
        print("7.导出外部文件并加密")
        #print("9.导入外部加密文件并解读")
        print("0.退出系统")
        print("=" * 30)

    CS1 = gro()
    while True:
        # 打印提示信息
        printMenu()
        key = input("请输入你要选择的操作：")
        if key == '0':
            exit()
        if key == '1':
            # 添加学生信息
            CS1.addstu_in()
        elif key == '2':
            CS1.del_itemin()
            # 删除学生信息
        elif key == '3':
            CS1.modifystu()
            # 修改学生信息
            # modifystu
        elif key == '4':
            CS1.sc_stu()
            # 查询学生信息
            # sc_stu
        elif key == '5':
            print("=" * 30)
            print("学生的信息如下：")
            print("序号  学号  姓名            成绩  ")
            i = 0
            for tempInfo in CS1.allstu:
                print("%d     %s     %s      %s"
                      % (i + 1, CS1.allstu[i].get('stuid'), CS1.allstu[i].get('stuname'),CS1.allstu[i].get('score')))
                i += 1
        elif key == '6':
            CS1.Output_txt()
            print("=" * 30)
            print("外部文件已导出...")
            # Output_txt
        elif key == '7':
            CS1.Input_txt()
            print("=" * 30)
            # Input_txt
            print("外部文件数据已导入...")
        elif key == '8':
            pass
            print("=" * 30)
            # Output_txt_s(stu_collection)
            print("外部加密文件已导出...")
        elif key == '9':
            pass
            print("=" * 30)
            # Input_txt_s(stu_collection)
            print("外部文件数据已解读...")


if __name__ == '__main__':
    main()

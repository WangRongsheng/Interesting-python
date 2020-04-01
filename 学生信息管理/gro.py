class stu:
    stuid = "001";
    stuname = "zhangsan";
    score = 80;

    def printstu(self):
        print(self.stuid)
        print(self.stuname)
        print(self.score)

    def savestudent(self):
        exmaple = {'stuid': 123, 'stuname': 'xxx', 'score': 100}
        temp = exmaple.fromkeys(['stuid', 'stuname', 'score'])
        temp['stuid'] = self.stuid
        temp['stuname'] = self.stuname
        temp['score'] = self.score
        return temp


class gro:
    allstu = []
    groname = 'CS1'

    def inputstu(self):
        newstu = stu()
        newstu.stuid = int(input("请输入学号:\n"))
        newstu.stuname = input("请输入学生姓名:\n")
        newstu.score = int(input("请输入成绩:\n"))
        newstu.savestudent()
        return newstu.savestudent()

    def addstu(self, stuobj):
        self.allstu.append(stuobj)

    def addstu_in(self):
        allnew = self.inputstu()
        self.addstu(allnew)

    def del_itemin(self):
        length = len(self.allstu)
        for s in range(length):
            if self.allstu[s]['stuid'] == int(input("输入删除学生的学号:\n")):
                self.allstu.pop(s)
            else:
                print("没有此学生相关信息!\n")
                break

    def modifystu(self):
        length = len(self.allstu)
        for s in range(length):
            if self.allstu[s].get('stuid') == int(input("输入修改的学生学号:\n")):
                self.allstu[s]['stuname'] = input("请输入预修改值(姓名):\n")
                self.allstu[s]['score'] = int(input("请输入预修改值(成绩):\n"))
                print("已修改!\n")
            else:
                print("没有此学生相关信息!")
                break

    def printallstu(self):  # 未使用
        for s in self.allstu:
            s.printstu()
            print("-" * 20)

    def sc_stu(self):
        length = len(self.allstu)
        for s in range(length):
            if self.allstu[s].get('stuid') == int(input("输入查询的学生学号:\n")):
                print(str(self.allstu[s].get('stuid')) +'  ' +str(self.allstu[s].get('stuname')) + '  ' +str(self.allstu[s].get('score')))
            else:
                print("没有此学生相关信息!")
                break

    def Output_txt(self):
        f = open("pydata.txt", "wt")
        length = len(self.allstu)
        for s in range(length):
            f.writelines(self.allstu[s] + "\n")

    def Input_txt(self):
        fw = open("pydata.txt", "rt")
        length = len(self.allstu)
        for line in fw:
            string = fw.readline()
            print(string)
            ts = string
            print(type(ts))
            for s in range(len(self.allstu)):
                if not (ts.get('stuid') == self.allstu[s].get('stuid')):
                    self.allstu.append(ts)
        print("读取成功!")

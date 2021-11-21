import sys
from zuowenapi import request1, request2#从API文件中导入函数
#导入相关的类
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QDesktopWidget, QPushButton, QMessageBox, QLineEdit, QColorDialog, QFontDialog, QTextEdit, QDialog, QLabel, QComboBox
from PyQt5.QtPrintSupport import QPageSetupDialog, QPrintDialog, QPrinter
# ----------------------------------
# 定义Example类
# ----------------------------------
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.printer = QPrinter()
        self.initUI()
        self.appkey = "*****************************"#从聚合数据处获得的APPKey
        self.result1 = {'comment':'','content':'','school':'','teacher':'','id':''}#储存精确查询结果
        self.result2 = {'totalCount': '', 'page': '', 'size': '', 'list': []}#储存查询结果
        #加入各个选项卡内容
        self.grade_warehouse = {'一年级': 11, '二年级': 12, '三年级': 13, '四年级': 14, '五年级': 15, '六年级': 16, '小升初': 17, '初一': 21, '初二': 22, '初三': 23, '中考': 24, '高一': 31, '高二': 32, '高三': 33, '高考': 34}
        self.rank_warehouse = {'优': 4, '良': 3, '中': 2, '差': 1}
        self.theme_warehouse = {'看图': 34, '游记': 31, '其他': 40, '状物': 14, '诗歌': 29, '写人': 11, '写景': 13, '童话': 25, '散文': 26, '小说': 24, '议论文': 15, '寓言': 28}
        self.word_number_warehouse = {'100字': 2, '200字': 4, '300字': 6, '400字': 8, '500字': 10, '600字': 12, '700字': 14, '800字': 16, '1000字': '18', '1200字': '19', '1200字以上': 20}

    def initUI(self):

        self.setWindowTitle('作文大全查询')#窗口名称
        self.id_providing = QTextEdit(self)#作文题目和id显示框
        self.composition_body = QTextEdit(self)#作文正文内容显示框
        # ----------------------------------
        # 加入各个查询按钮
        # ----------------------------------
        self.bt1 = QPushButton('选择字体', self)#更改作文字体按钮
        self.bt2 = QPushButton('选择颜色', self)#更改作文字体颜色按钮
        self.bt3 = QPushButton('页面设置', self)#选择页面设置按钮
        self.bt4 = QPushButton('打印文档', self)#选择打印文档按钮
        self.bt5 = QPushButton('关于', self)#产品信息按钮
        self.bt6 = QPushButton('查询', self)#查询作文信息按钮
        self.bt7 = QPushButton('精确查询', self)#根据编号精确查询作文信息按钮
        self.bt8 = QPushButton('打印文档', self)#打印精确查询结果按钮
        # ----------------------------------
        # 连接各个事件与信号槽
        # ----------------------------------
        self.bt1.clicked.connect(self.choicefont)
        self.bt2.clicked.connect(self.choicecolor)
        self.bt3.clicked.connect(self.pagesettings)
        self.bt4.clicked.connect(self.print_id_providing)
        self.bt5.clicked.connect(self.about)
        self.bt6.clicked.connect(self.access_id)
        self.bt7.clicked.connect(self.ask_composition)
        self.bt8.clicked.connect(self.print_composition)
        # ----------------------------------
        # 加入年级选项
        # ----------------------------------
        self.gradelabel = QLabel('年级:', self)
        self.Grade_combo = QComboBox(self)
        self.Grade_combo.resize(15, 15)
        self.Grade_combo.addItem("一年级")
        self.Grade_combo.addItem("二年级")
        self.Grade_combo.addItem("三年级")
        self.Grade_combo.addItem("四年级")
        self.Grade_combo.addItem("五年级")
        self.Grade_combo.addItem("六年级")
        self.Grade_combo.addItem("小升初")
        self.Grade_combo.addItem("初一")
        self.Grade_combo.addItem("初二")
        self.Grade_combo.addItem("初三")
        self.Grade_combo.addItem("中考")
        self.Grade_combo.addItem("高一")
        self.Grade_combo.addItem("高二")
        self.Grade_combo.addItem("高三")
        self.Grade_combo.addItem("高考")
        # ----------------------------------
        # 加入作文题材选项
        # ----------------------------------
        self.themelabel = QLabel('题材:', self)
        self.Theme_combo = QComboBox(self)
        self.Theme_combo.addItem("看图")
        self.Theme_combo.addItem("游记")
        self.Theme_combo.addItem("其他")
        self.Theme_combo.addItem("状物")
        self.Theme_combo.addItem("诗歌")
        self.Theme_combo.addItem("写人")
        self.Theme_combo.addItem("写景")
        self.Theme_combo.addItem("童话")
        self.Theme_combo.addItem("散文")
        self.Theme_combo.addItem("小说")
        self.Theme_combo.addItem("议论文")
        self.Theme_combo.addItem("寓言")
        # ----------------------------------
        # 加入作文字数选项
        # ----------------------------------
        self.word_numberlabel = QLabel('字数:', self)
        self.Word_number_combo = QComboBox(self)
        self.Word_number_combo.addItem("100字")
        self.Word_number_combo.addItem("200字")
        self.Word_number_combo.addItem("300字")
        self.Word_number_combo.addItem("400字")
        self.Word_number_combo.addItem("500字")
        self.Word_number_combo.addItem("600字")
        self.Word_number_combo.addItem("700字")
        self.Word_number_combo.addItem("800字")
        self.Word_number_combo.addItem("1000字")
        self.Word_number_combo.addItem("1200字")
        self.Word_number_combo.addItem("1200字以上")
        # ----------------------------------
        # 加入作文等级选项
        # ----------------------------------
        self.ranklable = QLabel('等级:', self)
        self.Rank_combo = QComboBox(self)
        self.Rank_combo.addItem("优")
        self.Rank_combo.addItem("良")
        self.Rank_combo.addItem("中")
        self.Rank_combo.addItem("差")
        # ----------------------------------
        # 加入依据作文编号精确查询选项
        # ----------------------------------
        self.id_request_label = QLabel('请输入作文编号:')
        self.id_request = QLineEdit('在这里输入作文编号', self)
        self.id_request.resize(15, 15)
        self.id_request.selectAll()
        self.id_request.setFocus()
        # ----------------------------------
        # 利用网格布局加入各个选项，设置间距为10个单位
        # ----------------------------------
        grid = QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(10)
        grid.addWidget(self.gradelabel, 1, 1)
        grid.addWidget(self.themelabel, 1, 3)
        grid.addWidget(self.word_numberlabel, 1, 5)
        grid.addWidget(self.ranklable, 1, 7)
        grid.addWidget(self.Grade_combo, 2, 1)
        grid.addWidget(self.Theme_combo, 2, 3)
        grid.addWidget(self.Word_number_combo, 2, 5)
        grid.addWidget(self.Rank_combo, 2, 7)
        grid.addWidget(self.bt6, 2, 9)
        grid.addWidget(self.id_providing, 3, 1, 5, 9)
        grid.addWidget(self.bt1, 9, 1)
        grid.addWidget(self.bt2, 9, 3)
        grid.addWidget(self.bt3, 9, 5)
        grid.addWidget(self.bt4, 9, 7)
        grid.addWidget(self.bt5, 9, 9)
        grid.addWidget(self.id_request_label, 13, 1)
        grid.addWidget(self.id_request, 10, 1, 10, 3)
        grid.addWidget(self.bt7, 14, 5)
        grid.addWidget(self.bt8, 14, 7)
        grid.addWidget(self.composition_body, 15, 1, 19, 9)
        #将窗口显示在屏幕中央
        self.show()
        self.center()
    # 页面设置函数
    def pagesettings(self):
        printsetdialog = QPageSetupDialog(self.printer, self)
        printsetdialog.exec_()

    # 打印作文题目id函数
    def print_id_providing(self):
        print_id_providing = QPrintDialog(self.printer, self)
        if QDialog.Accepted == print_id_providing.exec_():
            self.id_providing.print(self.printer)

    # 打印作文内容函数
    def print_composition(self):
        print_composition = QPrintDialog(self.printer, self)
        if QDialog.Accepted == print_composition.exec_():
            self.composition_body.print(self.printer)

    # 询问是否确定退出
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    #选择字体格式函数
    def choicefont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.id_providing.setCurrentFont(font)
            self.composition_body.setCurrentFont(font)

    # 选择字体颜色函数
    def choicecolor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.id_providing.setTextColor(col)
            self.composition_body.setTextColor(col)

    # 关于作者及创作信息
    def about(self):
        msgBox = QMessageBox(QMessageBox.NoIcon, '关于', '本作品可以查询下至小学一年级，上至高中三年级的优秀作文。\n本作品是python课程作品之一，请不要用于商业用途，如要使用，请联系作者;否则侵权必究！\n作者qq:1461471255')
        msgBox.exec()

    # 将页面显示在中央
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    #定义ask_compositon函数获取精确查询结果
    def ask_composition(self):
        id = int(self.id_request.text())#从id输入文本框中获取输入的id值
        self.result1 = request2(self.appkey, id)#调用request2函数查询作文内容
        #将作文内容显示在composition_body文本框中
        if self.result1 == 0:
            self.composition_body.setText("无此作文id!请换一个id试试!")
        else:
            self.composition_body.setText(self.result1['content'])

    #定义accecc_id函数获取作文id
    def access_id(self):
        #从年级、主题、等级和字数选项框中获取当前值
        value_grade = self.Grade_combo.currentText()
        value_theme = self.Theme_combo.currentText()
        value_rank = self.Rank_combo.currentText()
        value_number = self.Word_number_combo.currentText()
        #查找当前内容所对应的id编号
        gradeid = self.grade_warehouse[value_grade]
        themeid = self.theme_warehouse[value_theme]
        rankid = self.rank_warehouse[value_rank]
        word_numberid = self.word_number_warehouse[value_number]
        #调用request1函数查询作文id
        self.result2 = request1(self.appkey, gradeid, themeid, rankid, word_numberid)
        #将所找到的作文题目和id显示在id_providing文本框中
        if self.result2 == 0:
            self.id_providing.setText("未查询到相关结果!\n再换一种试试呀!")
        else:
            n = len(self.result2['list'])
            string ='题目:'+self.result2['list'][0]['name'] + ' id是:' + str(self.result2['list'][0]['id'])+'\n'
            i = 1
            while i < n:
                string = string + '题目:'+self.result2['list'][i]['name'] + ' id是:' + str(self.result2['list'][i]['id'])+'\n'
                i+=1
            self.id_providing.setText(string)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-
 
# Form implementation generated from reading ui file 'fiction_reader.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
 
 
from PyQt5 import QtCore, QtGui, QtWidgets
# 添加代码
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import os
import sys
import requests
import re
 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(39, 20, 421, 131))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 36, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 86, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(282, 36, 101, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(120, 31, 161, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 81, 161, 28))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(288, 83, 51, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 83, 51, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(39, 175, 421, 231))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(5, 5, 405, 197))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)  # 修改成两列
        self.tableWidget.setRowCount(0)
        # 添加代码（第一个tab分成两列）
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(0, 130)  # 设置第一列宽度
        self.tableWidget.horizontalHeader().setStretchLastSection(True)  # 设置自动填充容器
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)  # 垂直滚动条
 
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(5, 5, 405, 197))
        self.listWidget.setObjectName("listWidget")
        # 添加代码
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode) # 图标格式显示
        self.listWidget.setIconSize(QtCore.QSize(50, 50))  # 图标大小
        self.listWidget.setMaximumWidth(405)  # 最大宽度
        self.listWidget.setSpacing(15)  # 间距大小
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)  # 垂直滚动条
 
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
 
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "阅读器"))
        self.groupBox.setTitle(_translate("MainWindow", "抓取设置"))
        self.label.setText(_translate("MainWindow", "请填写小说书号："))
        # 添加代码（设置默认书号）
        book_number = '5_5871'
        self.lineEdit.setText(_translate("MainWindow", book_number))  # 设置默认书号
 
        self.label_2.setText(_translate("MainWindow", "请选择保存路径："))
        # 添加代码（设置默认路径为当前程序路径下的file文件夹下）
        self.lineEdit_2.setText(_translate("MainWindow", os.getcwd() + '\\file'))
 
        self.label_3.setText(_translate("MainWindow", "（比如5_5871）"))
        self.pushButton.setText(_translate("MainWindow", "选择"))
        self.pushButton_2.setText(_translate("MainWindow", "确定"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "列表显示"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "图表显示"))
        # 添加代码（设置列表标题）
        item = self.tableWidget.horizontalHeaderItem(0)  # 获取表格的第一列
        item.setText(_translate("MainWindow", "书号"))  # 设置表格第一列的标题
        item = self.tableWidget.horizontalHeaderItem(1)  # 获取表格的第二列
        item.setText(_translate("MainWindow", "名称"))  # 设置表格第二列的标题
 
        self.pushButton.clicked.connect(self.msg)  # 为选择按钮绑定事件
        self.pushButton_2.clicked.connect(self.getDatas)  # 点击确定获取数据
 
    # 添加代码（选择保存路径）
    def msg(self):
        try:
            # dir_path即为选择的文件夹的绝对路径，第二形参为对话框标题，第三个为对话框打开后默认的路径
            self.dir_path = QFileDialog.getExistingDirectory(None, "选择路径", os.getcwd())
            self.lineEdit_2.setText(self.dir_path)  # 显示选择的保存路径
        except Exception as e:
            print(e)
 
    # 抓取所有数据
    def getDatas(self):
        try:
            try:
                while True:  # 无限循环（执行这个，才能爬取完显示）
                    self.book_number = self.lineEdit.text()  # 记录用户设置的书号
                    self.baseurl = 'https://www.booktxt.net/' + self.book_number + '/'  # 设置书本初始地址
                    self.getData(self.baseurl, self.lineEdit_2.text())  # 执行主方法
            except Exception:
                pass
            self.getFiles()  # 获取所有文件
            self.bindList()  # 对列表进行绑定
            self.bindTable()  # 对表格进行绑定
            self.listWidget.itemClicked.connect(self.itemClick)  # 绑定列表单击方法
            self.tableWidget.itemClicked.connect(self.tableClick)  # 绑定表格单击方法
        except Exception:
            QMessageBox.warning(None, "警告", "没有数据，请重新设置书号……", QMessageBox.Ok)
            return
 
    # 抓取数据
    def getData(self, url, path):
        html = self.urlTotext(url)
        dl = re.findall(r'id="list".*?</dl>', html, re.S)[0]
        links = re.findall(r'<a href="(.*?)">', dl)
        path = path + "\\" + self.book_number + "\\"  # 设置文章存储路径
        if not os.path.isdir(path):  # 判断路径是否存在
            os.mkdir(path)  # 创建路径
        for item in links[8:20]:  # 遍历文章列表
            # print(item)
            serial_number = item[0:-5]
            print(serial_number)
            articleUrl = self.baseurl + item  # 获取遍历到的具体文章地址
            articleHtml = self.urlTotext(articleUrl)
            # 提取章节内容
            article_content = re.findall(r'id="content">(.*?)</div>', articleHtml, re.S)[0]
            # 过滤掉内容的间隔符、换行符等
            article_content = article_content.replace('<br /><br />', '')
            article_content = article_content.replace('</br>', '')
            article_content = article_content.replace('&nbsp;', '')
 
            title = re.findall(r'<h1>(.*?)</h1>', articleHtml, re.S)[0]  # 获取文章标题
            fileName = path + serial_number + title + '.txt'  # 设置文章保存路径（包括文章名）
            newFile = open(fileName, "w")  # 打开或者创建文件
            newFile.write("<<" + title + ">>\n\n")  # 向文件中写入标题并换行
            newFile.write(article_content)  # 向文件中写入内容
            newFile.close()  # 关闭文件
        QMessageBox.Information(None, "提示", self.book_number + "的小说保存完成", QMessageBox.Ok)
 
    # 从网页提取数据
    def urlTotext(self, url):
        response = requests.get(url)
        # 编码方式
        response.encoding = 'gbk'
        html = response.text
        return html
 
    # 获取所有文件
    def getFiles(self):
        self.list = os.listdir(self.lineEdit_2.text() + '\\' + self.lineEdit.text())  # 列出文件夹下所有的目录与文件
        self.list = sorted(self.list) # 排序
        print(self.list)
 
    # 将文件显示在Table中（列表显示）
    def bindTable(self):
        for i in range(0, len(self.list)):  # 遍历文件列表
            self.tableWidget.insertRow(i)  # 添加新行
            # 设置第一列的值为书号
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(self.lineEdit.text()))
            # 设置第二列的值为文件名
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(self.list[i]))
 
    # 表格单击方法，用来打开选中的项
    def tableClick(self, item):
        if 'txt' in item.text(): # 点击文件名才弹出
            os.startfile(self.lineEdit_2.text() + '\\' + self.lineEdit.text() + '\\' + item.text())
 
    # 将文件显示在List列表中（图表显示）
    def bindList(self):
        for i in range(0, len(self.list)):  # 遍历文件列表
            self.item = QtWidgets.QListWidgetItem(self.listWidget)  # 创建列表项
            self.item.setIcon(QtGui.QIcon('images/fiction.png'))  # 设置列表项图标
            self.item.setText(str(self.list[i])[7:13] + '...')  # 截取字符串（不显示序号）
            self.item.setToolTip(self.list[i])  # 设置提示文字
            self.item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # 设置选中与否
    # 列表单击方法，用来打开选中的项
    def itemClick(self, item):
        os.startfile(self.lineEdit_2.text() + '\\' + self.lineEdit.text() + '\\' + item.toolTip())
# 主方法（添加代码）
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = Ui_MainWindow()  # 创建PyQt设计的窗体对象
    ui.setupUi(MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
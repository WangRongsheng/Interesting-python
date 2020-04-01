import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random
import requests
from bs4 import BeautifulSoup
import threading
import pandas as pd
import datetime
data = pd.read_excel('全国身份证号对应省市区.xls', header=None, names=['身份证前六位', '所属地区'])
gender_id = {'0': '女', '1': '男'}
class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("全国身份证号验证及查询系统")
        self.layout = QGridLayout()
        self.setLayout(self.layout)  # 局部布局

        self.titleText = QTextBrowser()
        self.titleText.setText('全国身份证号验证及查询系统')
        self.titleText.setStyleSheet(
            "font-size:24px;font-weight:700;background:white;background-color: rgba(255,255,255,255);border: none;color:#0000CD")
        self.titleText.setAlignment(Qt.AlignCenter)
        self.titleText.setFixedSize(500, 40)
        self.layout.addWidget(self.titleText, 0, 0, 1, 3 , Qt.AlignCenter)
        self.Text = QTextBrowser()
        self.Text.setText('请输入身份证号码：')
        self.Text.setAlignment(Qt.AlignRight)
        self.Text.setStyleSheet(
            "vertical-align:middle;font-size:18px;font-weight:700;background:white;background-color: rgba(255,255,255,255);border: none;color:#FFA500")
        self.Text.setFixedSize(180, 30)
        self.layout.addWidget(self.Text, 1, 0, Qt.AlignRight)

        self.idcardText = QLineEdit(self)
        self.idcardText.setFixedSize(210, 30)
        self.idcardText.setStyleSheet("font-size:16px;font-weight:500;background-color: rgba(255,255,255,180);border: none;color:#55007f")
        self.layout.addWidget(self.idcardText, 1, 1, Qt.AlignLeft)

        self.Text = QTextBrowser()
        self.Text.setText('查询结果：')
        self.Text.setAlignment(Qt.AlignRight)
        self.Text.setStyleSheet(
            "font-size:18px;font-weight:700;background:white;background-color: rgba(255,255,255,255);border: none;color:#FFA500")
        self.Text.setFixedSize(105, 30)
        self.layout.addWidget(self.Text, 2, 0, Qt.AlignRight)

        self.resultText = QLineEdit(self)
        self.resultText.setFixedSize(210, 25)
        self.resultText.setStyleSheet(
            "font-size:16px;font-weight:500;background-color: rgba(255,255,255,180);border: none;color:#55007f")
        self.layout.addWidget(self.resultText, 2, 1, Qt.AlignLeft)

        self.Text = QTextBrowser()
        self.Text.setText('性别：')
        self.Text.setAlignment(Qt.AlignRight)
        self.Text.setStyleSheet(
            "font-size:18px;font-weight:700;background:white;background-color: rgba(255,255,255,255);border: none;color:#FFA500")
        self.Text.setFixedSize(65, 30)
        self.layout.addWidget(self.Text, 3, 0, Qt.AlignRight)

        self.genderText = QLineEdit(self)
        self.genderText.setFixedSize(210, 25)
        self.genderText.setStyleSheet(
            "font-size:16px;font-weight:500;background-color: rgba(255,255,255,180);border: none;color:#55007f")
        self.layout.addWidget(self.genderText, 3, 1, Qt.AlignLeft)

        self.Text = QTextBrowser()
        self.Text.setText('年龄：')
        self.Text.setAlignment(Qt.AlignRight)
        self.Text.setStyleSheet(
            "font-size:18px;font-weight:700;background:white;background-color: rgba(255,255,255,255);border: none;color:#FFA500")
        self.Text.setFixedSize(65, 30)
        self.layout.addWidget(self.Text, 4, 0, Qt.AlignRight)

        self.ageText = QLineEdit(self)
        self.ageText.setFixedSize(210, 25)
        self.ageText.setStyleSheet(
            "font-size:16px;font-weight:500;background-color: rgba(255,255,255,180);border: none;color:#55007f")
        self.layout.addWidget(self.ageText, 4, 1, Qt.AlignLeft)

        self.Text = QTextBrowser()
        self.Text.setText('发证地：')
        self.Text.setAlignment(Qt.AlignRight)
        self.Text.setStyleSheet(
            "font-size:18px;font-weight:700;background:white;background-color: rgba(255,255,255,255);border: none;color:#FFA500")
        self.Text.setFixedSize(85, 30)
        self.layout.addWidget(self.Text, 5, 0, Qt.AlignRight)

        self.addressText = QLineEdit(self)
        self.addressText.setFixedSize(210, 25)
        self.addressText.setStyleSheet(
            "font-size:16px;font-weight:500;background-color: rgba(255,255,255,180);border: none;color:#55007f")
        self.layout.addWidget(self.addressText, 5, 1, Qt.AlignLeft)

        self.startPushButton = QPushButton("开始查询")
        self.startPushButton.setFixedSize(70, 60)
        self.startPushButton.clicked.connect(self.check)
        self.layout.addWidget(self.startPushButton, 3, 2, 2, 2, Qt.AlignRight)

    def check(self):
        idcard = self.idcardText.text()
        verification = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        sum = 0
        for i, j in zip(list(idcard)[0:18], verification):
            sum += int(i) * j
        final_dic = {0: 1, 1: 0, 2: 'X', 3: 9, 4: 8, 5: 7, 6: 6, 7: 5, 8: 4, 9: 3, 10: 2}
        if str(final_dic[sum % 11]) == str(idcard[17]):
            self.resultText.setText('验证成功')
        else:
            self.resultText.setText('验证失败')
        gender_id = {'0': '女', '1': '男'}
        gender = gender_id[str(int(idcard[16]) % 2)]
        age = int(datetime.datetime.now().year) - int(idcard[6:10])
        address = data[data['身份证前六位'].eq(idcard[:6])]['所属地区']

        self.genderText.setText(gender)
        self.ageText.setText(str(age))
        self.addressText.setText(str(address.values[0]))
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
app = QApplication(sys.argv)
show = Window()  #主窗口的类
palette = QPalette()
palette.setBrush(QPalette.Background, QBrush(QPixmap("派大星.png")))
show.setFixedSize(500, 250)
show.setPalette(palette)
show.show()
sys.exit(app.exec_())
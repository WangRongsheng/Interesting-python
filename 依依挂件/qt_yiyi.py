import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Qt_pet(QWidget):

    def __init__(self):
        super(Qt_pet, self).__init__()

        self.dis_file = "yiyi"
        self.windowinit()
        self.icon_quit()

        self.pos_first = self.pos()
        self.img_count = len(os.listdir('./image/{}'.format(self.dis_file)))
        self.timer = QTimer()
        self.timer.timeout.connect(self.img_update)
        self.timer.start(100)


    def img_update(self):
        if self.img_num < self.img_count:
            self.img_num += 1
        else:
            self.img_num = 0
        self.img_path = './image/{file}/{img}.png'.format(file=self.dis_file, img=str(self.img_num))
        self.qpixmap = QPixmap(self.img_path)
        self.lab.setPixmap(self.qpixmap)

    def windowinit(self):
        self.x = 1800
        self.y = 800
        self.setGeometry(self.x, self.y, 300, 300)
        self.setWindowTitle('My Pet')
        self.img_num = 1
        self.img_path = './image/{file}/{img}.png'.format(file=self.dis_file, img=str(self.img_num))
        self.lab = QLabel(self)
        self.qpixmap = QPixmap(self.img_path)
        self.lab.setPixmap(self.qpixmap)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def icon_quit(self):
        mini_icon = QSystemTrayIcon(self)
        mini_icon.setIcon(QIcon('./image/img3/1.png'))
        quit_menu = QAction('Exit', self, triggered=self.quit)
        tpMenu = QMenu(self)
        tpMenu.addAction(quit_menu)
        mini_icon.setContextMenu(tpMenu)
        mini_icon.show()

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.pos_first = QMouseEvent.globalPos() - self.pos()
            QMouseEvent.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.pos_first)
            print(self.pos())
            self.x, self.y = self.pos().x, self.pos().y
            QMouseEvent.accept()

    def quit(self):
        self.close()
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pet = Qt_pet()
    sys.exit(app.exec_())

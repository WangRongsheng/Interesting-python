"""
俄罗斯方块的主界面
"""
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QMessageBox
from Board import Board


class Tetris(QMainWindow):
    # 继承QMainWindow类实现游戏的主界面

    def __init__(self):
        # 类的初始化

        # 加一个suppress规则，消除pycharm的黄色警告，否则会警告__init__():
        # noinspection PyArgumentList
        super(Tetris, self).__init__()  # 父类初始化

        self.board = Board(self)  # 创建Board实例
        self.setCentralWidget(self.board)  # 设置为应用程序的核心部件
        self.init_board()  # 初始化board
        self.init_ui()  # 初始化GUI

    def init_board(self):
        # 将得分显示在状态栏
        self.board.msg2Statusbar[str].connect(self.statusBar().showMessage)

        # 游戏开始
        self.board.start()

    def init_ui(self):
        # 界面的基本信息设置
        self.resize(180, 380)  # 界面尺寸180 * 380
        self.center()  # 根据用户屏幕大小将游戏居中
        self.setWindowTitle('Tetris')  # 设置窗口标题
        self.show()  # 显示窗口

    def center(self):
        # 根据用户屏幕大小将游戏居中
        screen = QDesktopWidget().screenGeometry()  # 用户屏幕
        size = self.geometry()  # 游戏窗口屏幕

        # move()函数调整位置，将游戏窗口居中
        self.move(int((screen.width() - size.width()) / 2),
                  int((screen.height() - size.height()) / 2))

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            'Quit',
            '确定要关闭俄罗斯方块吗？',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

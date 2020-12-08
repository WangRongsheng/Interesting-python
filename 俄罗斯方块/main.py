"""
PyQt5实现俄罗斯方块

author：张艺川
last edit time：2019年10月3号

参考：http://code.py40.com/2052.html

在比赛开始后立即启动
我们可以通过按p键暂停游戏
左右键移动方块
上下键旋转方块
D键加速下落
空格键立即将方块下落至底部
分数是已经删除的行数，显示在左下角

Tetrominoe.py定义8种方块的索引，用0-7表示
Shape.py使用Terominoe.py中的索引，封装了方块的坐标和形状，以及相应的方法
Board.py实现了游戏主要的逻辑
Tetris.py使用pyqt5定义游戏界面、窗口
main.py是游戏的入口，直接运行即可开始游戏

"""
import sys
from PyQt5.QtWidgets import QApplication
from Tetris import Tetris


if __name__ == '__main__':

    # 每一pyqt5应用程序必须创建一个应用程序对象
    # sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)

    # 实例化Tetris()
    tetris = Tetris()

    # 系统exit()方法确保应用程序干净的退出
    sys.exit(app.exec_())

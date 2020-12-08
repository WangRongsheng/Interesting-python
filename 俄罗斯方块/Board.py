"""
Board创建一个面板类的实例
实现游戏的逻辑
"""
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import pyqtSignal, QBasicTimer, Qt
from PyQt5.QtGui import QPainter, QColor
from Tetrominoe import Tetrominoe
from Shape import Shape


class Board(QFrame):
    # 自定义信号，将信息展示在状态栏
    msg2Statusbar = pyqtSignal(str)

    # 定义常量值
    BoardWidth = 10  # 块的宽度
    BoardHeight = 22  # 块的长度
    Speed = 300  # 下落的速度，即timer循环刷新速度

    def __init__(self, parent):
        # noinspection PyArgumentList
        super().__init__(parent)

        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False

        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []  # 0到7的数字列表，表示面板上的形状和位置

        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clear_board()

    def shape_at(self, x, y):
        return self.board[(y * Board.BoardWidth) + x]

    def set_shape_at(self, x, y, shape):
        self.board[(y * Board.BoardWidth) + x] = shape

    # 因为界面Board大小可以动态调整，所以方块的大小也要随着改变
    def square_width(self):
        return self.contentsRect().width() // Board.BoardWidth

    def square_height(self):
        return self.contentsRect().height() // Board.BoardHeight

    def start(self):

        if self.isPaused:
            return

        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clear_board()

        self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.new_piece()
        self.timer.start(Board.Speed, self)

    def pause(self):

        if not self.isStarted:
            return

        self.isPaused = not self.isPaused

        if self.isPaused:
            self.timer.stop()
            self.msg2Statusbar.emit("paused")

        else:
            self.timer.start(Board.Speed, self)
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        rect = self.contentsRect()

        board_top = rect.bottom() - Board.BoardHeight * self.square_height()

        # 首先绘制所有已经落下去的方块
        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                shape = self.shape_at(j, Board.BoardHeight - i - 1)

                if shape != Tetrominoe.NoShape:
                    self.draw_square(painter,
                                     rect.left() + j * self.square_width(),
                                     board_top + i * self.square_height(), shape)

        # 绘制正在下降的方块
        if self.curPiece.shape() != Tetrominoe.NoShape:

            for i in range(4):
                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.draw_square(painter, rect.left() + x * self.square_width(),
                                 board_top + (Board.BoardHeight - y - 1) * self.square_height(),
                                 self.curPiece.shape())

    def keyPressEvent(self, event):

        if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
            super(Board, self).keyPressEvent(event)
            return

        key = event.key()

        # p键暂停
        if key == Qt.Key_P:
            self.pause()
            return

        if self.isPaused:
            return

        # 左右移动
        elif key == Qt.Key_Left:
            self.try_move(self.curPiece, self.curX - 1, self.curY)

        elif key == Qt.Key_Right:
            self.try_move(self.curPiece, self.curX + 1, self.curY)

        # 旋转
        elif key == Qt.Key_Down:
            self.try_move(self.curPiece.rotate_right(), self.curX, self.curY)

        elif key == Qt.Key_Up:
            self.try_move(self.curPiece.rotate_left(), self.curX, self.curY)

        # 下降到底部
        elif key == Qt.Key_Space:
            self.drop_down()

        # 加速
        elif key == Qt.Key_D:
            self.one_line_down()

        else:
            super(Board, self).keyPressEvent(event)

    def timerEvent(self, event):
        """
        时间事件
        当前一个方块降落到底部后，创建一个新的方块
        """
        if event.timerId() == self.timer.timerId():

            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.new_piece()
            else:
                self.one_line_down()

        else:
            super(Board, self).timerEvent(event)

    def clear_board(self):
        """通过设置Tetrominoe.NoShape清除面板"""
        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Tetrominoe.NoShape)

    def drop_down(self):

        new_y = self.curY

        while new_y > 0:

            if not self.try_move(self.curPiece, self.curX, new_y - 1):
                break

            new_y -= 1

        self.piece_dropped()

    def one_line_down(self):

        if not self.try_move(self.curPiece, self.curX, self.curY - 1):
            self.piece_dropped()

    def piece_dropped(self):

        for i in range(4):
            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.set_shape_at(x, y, self.curPiece.shape())

        self.remove_full_lines()

        if not self.isWaitingAfterLine:
            self.new_piece()

    def remove_full_lines(self):
        """
        如果到达底部,会调用removeFullLines()方法。
        我们会检查所有完整的线条然后删除它们。
        然后移动所有行高于当前删除整行一行。
        请注意,我们反的顺序行被删除。否则,就会出错。
        """
        num_full_lines = 0
        rows_to_remove = []

        for i in range(Board.BoardHeight):

            n = 0
            for j in range(Board.BoardWidth):
                if not self.shape_at(j, i) == Tetrominoe.NoShape:
                    n = n + 1

            if n == 10:
                rows_to_remove.append(i)

        rows_to_remove.reverse()  # 反转

        for m in rows_to_remove:

            for k in range(m, Board.BoardHeight):
                for l in range(Board.BoardWidth):
                    self.set_shape_at(l, k, self.shape_at(l, k + 1))

        num_full_lines = num_full_lines + len(rows_to_remove)

        if num_full_lines > 0:
            self.numLinesRemoved = self.numLinesRemoved + num_full_lines
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

            self.isWaitingAfterLine = True
            self.curPiece.set_shape(Tetrominoe.NoShape)
            self.update()

    def new_piece(self):
        """
        通过newPiece()方法创建一个新的方块
        如果不能进入它的初始位置,游戏就结束

        """
        self.curPiece = Shape()
        self.curPiece.set_random_shape()
        self.curX = Board.BoardWidth // 2 + 1
        self.curY = Board.BoardHeight - 1 + self.curPiece.min_y()

        if not self.try_move(self.curPiece, self.curX, self.curY):
            self.curPiece.set_shape(Tetrominoe.NoShape)
            self.timer.stop()
            self.isStarted = False
            self.msg2Statusbar.emit("Game over")

    def try_move(self, new_piece, new_x, new_y):
        """
        使用tryMove()方法尝试移动方块。
        如果方块的边缘已经接触到面板边缘或者不能移动,我们返回False。
        否则我们当前块下降到一个新的位置。
        """
        for i in range(4):

            x = new_x + new_piece.x(i)
            y = new_y - new_piece.y(i)

            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False

            if self.shape_at(x, y) != Tetrominoe.NoShape:
                return False

        self.curPiece = new_piece
        self.curX = new_x
        self.curY = new_y
        self.update()

        return True

    def draw_square(self, painter, x, y, shape):

        color_table = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                       0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QColor(color_table[shape])
        painter.fillRect(x + 1, y + 1, self.square_width() - 2,
                         self.square_height() - 2, color)

        painter.setPen(color.lighter())
        painter.drawLine(x, y + self.square_height() - 1, x, y)
        painter.drawLine(x, y, x + self.square_width() - 1, y)

        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.square_height() - 1,
                         x + self.square_width() - 1, y + self.square_height() - 1)
        painter.drawLine(x + self.square_width() - 1,
                         y + self.square_height() - 1, x + self.square_width() - 1, y + 1)

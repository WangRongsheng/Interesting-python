"""
定义不同方块的具体坐标，以及其基本的方法
"""
from Tetrominoe import Tetrominoe
from random import randint


class Shape(object):

    # 用四个点的坐标表示一种方块的坐标表示
    coordsTable = (
        ((0, 0), (0, 0), (0, 0), (0, 0)),
        ((0, -1), (0, 0), (-1, 0), (-1, 1)),
        ((0, -1), (0, 0), (1, 0), (1, 1)),
        ((0, -1), (0, 0), (0, 1), (0, 2)),
        ((-1, 0), (0, 0), (1, 0), (0, 1)),
        ((0, 0), (1, 0), (0, 1), (1, 1)),
        ((-1, -1), (0, -1), (0, 0), (0, 1)),
        ((1, -1), (0, -1), (0, 0), (0, 1))
    )

    def __init__(self):

        # 初始的方块是NoShape
        self.coords = [[0, 0] for _ in range(4)]
        self.pieceShape = Tetrominoe.NoShape
        self.set_shape(Tetrominoe.NoShape)

    def shape(self):
        # 返回shape类型
        return self.pieceShape

    def set_shape(self, shape):
        # 设置shape，同时修改coords
        table = Shape.coordsTable[shape]

        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]

        self.pieceShape = shape

    def set_random_shape(self):
        # 随机设置初始化的方块为一个特定方块
        self.set_shape(randint(1, 7))

    # 获得和设置x，y
    def x(self, index):
        return self.coords[index][0]

    def y(self, index):
        return self.coords[index][1]

    def set_x(self, index, x):
        self.coords[index][0] = x

    def set_y(self, index, y):
        self.coords[index][1] = y

    # 最小的y，在Board.py种使用
    def min_y(self):

        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])

        return m

    # 左旋和右旋
    def rotate_left(self):

        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape

        for i in range(4):
            result.set_x(i, self.y(i))
            result.set_y(i, -self.x(i))

        return result

    def rotate_right(self):

        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape

        for i in range(4):
            result.set_x(i, -self.y(i))
            result.set_y(i, self.x(i))

        return result

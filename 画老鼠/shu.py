import turtle

def head():
    turtle.color('black')

    # 脸轮廓
    turtle.pd() # 落笔
    turtle.circle(50) # 画一个半径为50的圆
    turtle.pu() # 提笔

    # 右耳轮廓
    turtle.goto(50,60) # 移动到x=50,y=60的位置
    turtle.pd() # 落笔
    turtle.circle(30,260) # 画一个半径为30，角度为245的圆弧
    turtle.pu() # 提笔
    # 右耳耳纹
    turtle.goto(30,90)
    turtle.pd()
    turtle.seth(65)
    turtle.circle(-30,70)
    turtle.pu()

    # 左耳轮廓
    turtle.goto(-50,60)
    turtle.pd()
    turtle.seth(180) # 设置方向为西，
    turtle.circle(-30,260)
    turtle.pu()
    # 左耳耳纹
    turtle.goto(-30,90)
    turtle.pd()
    turtle.seth(120)
    turtle.circle(30,70)
    turtle.pu()

    # 面部五官
    # 右侧眉毛
    turtle.goto(5,80)
    turtle.seth(20)
    turtle.pd()
    turtle.circle(-25,40)
    turtle.pu()
    # 左侧眉毛
    turtle.goto(-5,80)
    turtle.seth(160)
    turtle.pd()
    turtle.circle(25,40)
    turtle.pu()

    # 右侧眼睛
    turtle.begin_poly()
    turtle.goto(8,60)
    turtle.seth(45)
    turtle.pd()
    turtle.circle(-15,120)
    turtle.pu()
    turtle.goto(8,60)
    turtle.seth(40)
    turtle.pd()
    turtle.circle(-15,100)
    turtle.pu()
    turtle.end_poly()

    # 左侧眼睛
    turtle.goto(-8,60)
    turtle.seth(135)
    turtle.pd()
    turtle.circle(15,120)
    turtle.pu()
    turtle.goto(-8,60)
    turtle.seth(140)
    turtle.pd()
    turtle.circle(15,100)
    turtle.pu()

    # 鼻子
    # 鼻子上瓣
    turtle.goto(-6,45)
    turtle.seth(70)
    turtle.pd()
    turtle.circle(-6,150)
    turtle.pu()
    # 鼻子下瓣
    turtle.goto(-6,45)
    turtle.seth(-70)
    turtle.pd()
    turtle.circle(6,150)
    turtle.pu()

    # 鼻线
    turtle.goto(0,40)
    turtle.seth(270)
    turtle.pd()
    turtle.forward(7)
    turtle.pu()

    # 上嘴线
    turtle.seth(200)
    turtle.pd()
    turtle.circle(-15,60)
    turtle.pu()

    turtle.goto(0,33)
    turtle.seth(-20)
    turtle.pd()
    turtle.circle(15,60)
    turtle.pu()

    # 下嘴线
    turtle.goto(10,33)
    turtle.seth(260)
    turtle.pd()
    turtle.circle(-15,65)
    turtle.pu()

    turtle.goto(-10,33)
    turtle.seth(280)
    turtle.pd()
    turtle.circle(15,65)
    turtle.pu()

    # 牙齿
    turtle.goto(4,33)
    turtle.seth(270)
    turtle.pd()
    turtle.forward(4)
    turtle.seth(180)
    turtle.forward(8)
    turtle.seth(90)
    turtle.forward(4)
    turtle.pu()

    # 胡须
    turtle.pensize(2)
    turtle.goto(30,30)
    turtle.seth(8)
    turtle.pd()
    turtle.circle(-60,40)
    turtle.pu()

    turtle.goto(30,25)
    turtle.seth(-5)
    turtle.pd()
    turtle.circle(-60,40)
    turtle.pu()


    turtle.goto(-30,30)
    turtle.seth(172)
    turtle.pd()
    turtle.circle(60,40)
    turtle.pu()

    turtle.goto(-30,25)
    turtle.seth(188)
    turtle.pd()
    turtle.circle(60,40)
    turtle.pu()

    # 睫毛
    turtle.pensize(1)
    turtle.goto(30,58)
    turtle.seth(20)
    turtle.pd()
    turtle.circle(20,20)
    turtle.pu()

    turtle.pensize(1)
    turtle.goto(28,62)
    turtle.seth(25)
    turtle.pd()
    turtle.circle(20,12)
    turtle.pu()

    turtle.pensize(1)
    turtle.goto(-30,58)
    turtle.seth(160)
    turtle.pd()
    turtle.circle(-20,20)
    turtle.pu()

    turtle.pensize(1)
    turtle.goto(-28,62)
    turtle.seth(165)
    turtle.pd()
    turtle.circle(-20,12)
    turtle.pu()


def body():
    # 左手
    turtle.goto(-25,8)
    turtle.seth(240)
    turtle.pd()
    turtle.circle(150,15)
    turtle.seth(270)
    turtle.circle(40,15)
    turtle.circle(15,65)
    turtle.seth(0)
    turtle.forward(10)
    turtle.circle(10,100)
    turtle.seth(90)
    turtle.forward(5)
    turtle.circle(10,100)
    turtle.seth(180)
    turtle.forward(10)
    turtle.pu()
    # 右手
    turtle.goto(25,8)
    turtle.seth(-60)
    turtle.pd()
    turtle.circle(-150,15)
    turtle.seth(270)
    turtle.circle(-40,15)
    turtle.circle(-15,65)
    turtle.seth(180)
    turtle.forward(10)
    turtle.circle(-10,100)
    turtle.seth(90)
    turtle.forward(5)
    turtle.circle(-10,100)
    turtle.seth(0)
    turtle.forward(10)
    turtle.pu()

    # 袍子
    turtle.goto(-30,-48)
    turtle.seth(270)
    turtle.pd()
    turtle.forward(30)
    turtle.circle(10,100)
    turtle.seth(0)
    turtle.forward(38)
    turtle.circle(10,100)
    turtle.seth(90)
    turtle.forward(30)
    turtle.pu()

    # 领口
    turtle.goto(-20,4)
    turtle.pd()
    turtle.seth(300)
    turtle.circle(30,20)
    turtle.seth(0)
    turtle.forward(25)
    turtle.seth(30)
    turtle.circle(30,20)
    turtle.pu()

    # 官带
    turtle.goto(-7,-38)
    turtle.seth(0)
    turtle.pd()
    turtle.forward(15)
    turtle.pu()
    turtle.goto(-30,-54)
    turtle.pd()
    turtle.forward(60)
    turtle.pu()

    # 袍子上的波浪
    turtle.goto(-30,-80)
    turtle.pd()
    turtle.seth(90)
    turtle.circle(-5,180)
    turtle.seth(90)
    turtle.circle(-5,180)
    turtle.seth(90)
    turtle.circle(-5,180)
    turtle.seth(90)
    turtle.circle(-5,180)
    turtle.seth(90)
    turtle.circle(-5,180)
    turtle.seth(90)
    turtle.circle(-5,180)
    turtle.pu()

    turtle.goto(-25,-85)
    turtle.pd()
    turtle.seth(90)
    turtle.circle(-5,180)
    turtle.seth(90)
    turtle.circle(-5,180)
    turtle.seth(90)
    turtle.circle(-5,180)
    turtle.seth(90)
    turtle.circle(-5,180)
    turtle.seth(90)
    turtle.circle(-5,180)
    turtle.pu()


def hands():
    turtle.goto(-8, -25)
    turtle.pd()
    turtle.seth(30)
    turtle.forward(10)
    turtle.seth(0)
    turtle.circle(-10, 50)
    turtle.seth(210)
    turtle.forward(18)

    turtle.back(10)
    turtle.seth(-45)
    turtle.forward(10)
    turtle.back(10)
    turtle.seth(30)
    turtle.forward(8)
    turtle.seth(300)
    turtle.forward(5)
    turtle.pu()

    turtle.goto(0, -75)
    turtle.pd()
    turtle.seth(0)
    turtle.circle(10)
    turtle.seth(90)
    turtle.circle(10, 90)
    turtle.seth(0)
    turtle.circle(10, 90)
    turtle.seth(270)
    turtle.circle(10, 90)
    turtle.seth(180)
    turtle.circle(10, 90)
    turtle.pu()


def hat():
    # 画帽子
    turtle.goto(-20,98)
    turtle.pd()
    turtle.seth(80)
    turtle.forward(20)
    turtle.seth(60)
    turtle.circle(-20,140)
    turtle.seth(-85)
    turtle.forward(18)
    turtle.pu()

    turtle.goto(-20,98)
    turtle.pd()
    turtle.seth(80)
    turtle.forward(5)
    turtle.seth(30)
    turtle.forward(22)
    turtle.seth(-25)
    turtle.forward(24)
    turtle.pu()

    turtle.goto(0,127)
    turtle.pd()
    turtle.seth(0)
    turtle.circle(5)
    turtle.pu()

    turtle.goto(0,125)
    turtle.pd()
    turtle.seth(270)
    turtle.forward(10)
    turtle.pu()

    # 右边抖带
    turtle.goto(19,110)
    turtle.pd()
    turtle.seth(30)
    turtle.circle(40,50)
    turtle.seth(0)
    turtle.circle(10)
    turtle.seth(90)
    turtle.circle(10,90)
    turtle.seth(0)
    turtle.circle(10,90)
    turtle.seth(270)
    turtle.circle(10,90)
    turtle.seth(180)
    turtle.circle(10,90)
    turtle.pu()

    # 左边抖带
    turtle.goto(-19,110)
    turtle.pd()
    turtle.seth(150)
    turtle.circle(-40,50)
    turtle.seth(0)
    turtle.circle(10)
    turtle.seth(90)
    turtle.circle(10,90)
    turtle.seth(0)
    turtle.circle(10,90)
    turtle.seth(270)
    turtle.circle(10,90)
    turtle.seth(180)
    turtle.circle(10,90)
    turtle.pu()

def tail():
    turtle.goto(30, -60)
    turtle.pd()
    turtle.seth(20)
    turtle.circle(40, 80)
    turtle.circle(-20, 180)
    turtle.circle(-10, 90)


if __name__ == '__main__':
    head()
    body()
    hands()
    hat()
    tail()
    turtle.done()

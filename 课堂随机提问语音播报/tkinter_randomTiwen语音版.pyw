import tkinter
from tkinter.messagebox import showinfo
from time import sleep
from random import shuffle
from itertools import cycle
from threading import Thread
try:
    from speech import say
    has_speech = True
except:
    has_speech = False

root = tkinter.Tk()
# 窗口标题
root.title('随机提问')
# 窗口初始大小和位置
root.geometry('260x180+400+300')
# 不允许改变窗口大小
root.resizable(False, False)

# 关闭程序时执行的函数代码，停止滚动显示学生名单
def closeWindow():
    if rolling.get():
        showinfo('不能关闭', '请先停止名单滚动')
        return
    root.destroy()
root.protocol('WM_DELETE_WINDOW', closeWindow)

# 读取学生名单，如果不存在文件就使用模拟数据
try:
    with open('学生名单.txt', encoding='utf8') as fp:
        students = fp.read().splitlines()
except:
    showinfo('学生名单不存在',
             '当前目录中没有文件：学生名单.txt\n临时使用模拟数据')
    students = ['张三', '李四', '王五', '赵六', '周七', '钱八']
    
# 变量，用来控制是否滚动显示学生名单
rolling = tkinter.BooleanVar(root, value=False)

def switch():
    rolling.set(True)
    # 随机打乱学生名单
    t = students[:]
    shuffle(t)
    t = cycle(t)
    
    while rolling.get():        
        # 滚动显示
        lbFirst['text'] = lbSecond['text']        
        lbSecond['text'] = lbThird['text']
        lbThird['text'] = next(t)
        
        # 数字可以修改，控制滚动速度
        sleep(0.1)
        
def btnStartClick():
    # 每次单击“开始”按钮启动新线程
    Thread(target=switch).start()
    btnStart['state'] = 'disabled'
    btnStop['state'] = 'normal'
btnStart = tkinter.Button(root,
                          text='开始',
                          command=btnStartClick)
btnStart.place(x=30, y=10, width=80, height=20)

saying = tkinter.BooleanVar(root, value=False)
def say_name():
    while has_speech and saying.get():
        say(f"请{lbSecond['text'].replace(',','')}回答问题")
        
def btnStopClick():
    # 单击“停”按钮结束滚动显示
    rolling.set(False)
    sleep(0.3)
    saying.set(True)
    Thread(target=say_name).start()
    showinfo('恭喜', '本次中奖：'+lbSecond['text'])
    saying.set(False)
    btnStart['state'] = 'normal'
    btnStop['state'] = 'disabled'
btnStop = tkinter.Button(root, text='停', command=btnStopClick)
btnStop['state'] = 'disabled'
btnStop.place(x=150, y=10, width=80, height=20)

# 用来滚动显示学生名单的3个Label组件
# 可以根据需要进行添加，但要修改上面的线程函数代码
lbFirst = tkinter.Label(root, text='')
lbFirst.place(x=80, y=60, width=100, height=20)

# 红色Label组件，表示中奖名单
lbSecond = tkinter.Label(root, text='')
lbSecond['fg'] = 'red'
lbSecond.place(x=80, y=90, width=100, height=20)

lbThird = tkinter.Label(root, text='')
lbThird.place(x=80, y=120, width=100, height=20)

# 启动tkinter主程序
root.mainloop()

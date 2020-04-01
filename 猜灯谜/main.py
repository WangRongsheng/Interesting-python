from tkinter import messagebox
from PIL import Image, ImageTk
import random
import csv
import tkinter as tk



class LanternRiddles(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("猜灯谜软件-《菜鸟学python》")
        self.root.geometry("1200x500")
        self.root.geometry("+100+150")
        self.data = []
        with open('new_data.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.data.append(row)
        self.index = [i for i in range(len(self.data))]
        random.shuffle(self.index)

        # 做成背景的装饰
        pic1 = Image.open('pic/bg.jpg').resize((1200, 500))  # 加载图片并调整大小至窗口大小
        pic = ImageTk.PhotoImage(pic1)
        render = tk.Label(self.root, image=pic, compound=tk.CENTER, justify=tk.LEFT)
        render.place(x=0, y=0)

        # 标签 and 输入框
        label = tk.Label(self.root, text='输入答案', font=('微软雅黑', 15), fg='black', bg="Magenta")
        label.place(x=0, y=10, width=100, height=40)
        self.entry = tk.Entry(self.root, font=('宋体', 15), width=15, bg="GhostWhite")
        self.entry.place(x=110, y=10, width=150, height=40)  # 设置输入框，输入答案
        # 按钮
        confirm_button = tk.Button(self.root, text='确认', font=('微软雅黑', 15), bg="LightGreen", command=self.check)
        confirm_button.place(x=270, y=10, width=100, height=40)  # 确定按钮

        quit_button = tk.Button(self.root, text='退出软件', font=('微软雅黑', 15), bg="LightGreen", command=self.quit)
        quit_button.place(x=800, y=10, width=100, height=40)  # 退出软件
        start_button = tk.Button(self.root, text='开始答题', font=('微软雅黑', 15), bg="LightGreen", command=self.get_next)
        start_button.place(x=0, y=80, width=100, height=40)  # 更换题目
        prompt_button = tk.Button(self.root, text='显示提示', font=('微软雅黑', 15), bg="LightGreen", command=self.show_prompt)
        prompt_button.place(x=650, y=10, width=100, height=40)  # 更换题目

        self.riddle = tk.Text(self.root, bg="OrangeRed", fg="dimgray",  font=('微软雅黑', 15))
        self.riddle.place(x=200, y=180, width=300, height=160)  # 显示题目

        self.root.mainloop()

    def get_next(self):  # 更换题目
        self.riddle.delete('1.0', 'end')  # 清空显示
        index = random.choice(self.index)
        self.index.remove(index)
        self.question = self.data[index][0]
        self.answer = self.data[index][1]
        self.prompt = self.data[index][2]
        self.riddle.insert(tk.END, self.question)

    def check(self):  # 验证答案
        reply = self.entry.get()
        if reply in self.answer:
            messagebox.showinfo('提示', '回答正确')
            self.get_next()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showinfo('提示', '回答错误，请重试')
            self.entry.delete(0, tk.END)

    def show_prompt(self):  # 显示提示
        messagebox.showinfo('提示', self.prompt)

    def quit(self):
        self.root.destroy()


if __name__ == '__main__':
    LanternRiddles()
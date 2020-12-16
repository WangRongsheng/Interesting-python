import tkinter as tk
from snownlp import SnowNLP
from utils import download_shuoshuo, save_result

window = tk.Tk()

window.title("空间说说情感分析")
window.geometry("750x600")

e = tk.Entry(window, width=80)
e.insert(0, "请复制你的cookie")
e.grid(row=0, column=0, columnspan=2)

def _download_shuoshuo():
    cookie = e.get()
    download_shuoshuo(cookie)
    e.delete(0, "end")
    e.insert(0, "请复制你的cookie")
    
b = tk.Button(window, text="获取说说数据", width=20, height=3, command=_download_shuoshuo)
b.grid(row=1, column=0)

def analyse_shuoshuo():
    global image_file
    sentence = e.get()
    path = "results/my_shuoshuo_sentiment.png"
    save_result(qq_msgs="inputs/msgs.txt", path=path)
    image_file = tk.PhotoImage(file=path)
    canvas.itemconfig(image, image=image_file)
    
b1 = tk.Button(window, text="分析", width=20, height=3, command=analyse_shuoshuo)
b1.grid(row=1, column=1)

canvas = tk.Canvas(window, height=500, width=700)
image_file = tk.PhotoImage(file="data/welcome.gif")
image = canvas.create_image(0, 0, anchor="nw", image=image_file)
canvas.grid(row=2, column=0, columnspan=2)

window.mainloop()

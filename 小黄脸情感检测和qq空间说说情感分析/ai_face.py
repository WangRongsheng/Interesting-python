import tkinter as tk
from snownlp import SnowNLP

def get_face_path(sentence):
    s = SnowNLP(sentence)
    score = s.sentiments
    if score < 0.25:
        path = "data/face_sad.png"
    elif score < 0.5:
        path = "data/face_unhappy.png"
    elif score < 0.75:
        path = "data/face_happy1.png"
    else:
        path = "data/face_happy2.png"
    return path

window = tk.Tk()

window.title("情绪判断")
window.geometry("350x300")

e = tk.Entry(window, width=37)
e.grid(row=0, column=0)

def my_func():
    global image_file
    sentence = e.get()
    path = get_face_path(sentence)
    image_file = tk.PhotoImage(file=path)
    canvas.itemconfig(image, image=image_file)
    
b = tk.Button(window, text="分析", width=20, height=3, command=my_func)
b.grid(row=1, column=0)

canvas = tk.Canvas(window, height=200, width=200)
image_file = tk.PhotoImage(file="data/welcome.gif")
image = canvas.create_image(100, 100, anchor="center", image=image_file)
canvas.grid(row=2, column=0)

window.mainloop()

import tkinter as tk

window = tk.Tk()

window.title("这是我的第一个小程序")
window.geometry("750x400")

e = tk.Entry(window, width=80)
e.grid(row=0, column=0, columnspan=2)

def my_func():
    e.insert("end", " 我拿到了这段文字")
b = tk.Button(window, text="我的功能", width=20, height=3, command=my_func)
b.grid(row=1, column=0)


lb = tk.Listbox(window, width=40)
lb.grid(row=2, column=0)

def move():
    var = e.get()
    lb.insert("end", var)
b2 = tk.Button(window, text="转移内容", width=20, height=3, command=move)
b2.grid(row=1, column=1)


canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file="data/welcome.gif")
image = canvas.create_image(0, 0, anchor="nw", image=image_file)
canvas.grid(row=3, column=0, columnspan=2)

image_file = tk.PhotoImage(file="data/face_happy1.png")
canvas.itemconfig(image, image=image_file)

window.mainloop()

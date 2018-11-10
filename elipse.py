"""
write by 高谦
"""
from tkinter import *
import turtle as tu
import math
root=Tk()
root.title("画椭圆")
Label(root,text="长轴").grid(row=0)
Label(root,text="短轴").grid(row=1)
e1=Entry(root)
e2=Entry(root)
e1.grid(row=0,column=1,padx=5,pady=5)
e2.grid(row=1,column=1,padx=5,pady=5)
def show():
    tu.screensize(1080, 720)
    tu.setup(startx=None, starty=None)
    tu.pencolor("red")

    def move(x, y):
        tu.penup()
        tu.goto(x, y)
        tu.pendown()
        tu.goto(x + 1, y + 1)

    def draw(x, y):
        move(x, y)
        move(x, -y)
        move(-x, y)
        move(-x, -y)
        tu.penup()
        tu.goto(x, y)
        tu.pendown()
    a = int(e1.get())
    b = int(e2.get())
    e1.delete(0, END)
    e2.delete(0, END)
    x = 0
    y = b
    d1 = b * b + a * a * (0.25 - b)
    draw(x, y)
    while b * b * (x + 1) < a * a * (y - 0.5):
        if d1 < 0:
            d1 += b * b * (x * 2 + 3)
            x += 1
        else:
            d1 += b * b * (x * 2 + 3) + a * a * (-2 * y + 2)
            x += 1
            y -= 1
        draw(x, y)
    d2 = math.sqrt(b * (x + 0.5)) + math.sqrt(a * (y - 1)) - math.sqrt(a * b)
    while y > 0:
        if d2 < 0:
            d2 += b * b * (x * 2 + 2) + a * a * (-2 * y + 3)
            x += 1
            y -= 1
        else:
            d2 += a * a * (-2 * y + 3)
            y -= 1
        draw(x, y)
    tu.mainloop()
Button(root,text="开始画图",width=10,command=show).grid(row=2,column=0,padx=5,pady=5)
Button(root,text="退出程序",width=10,command=root.quit).grid(row=2,column=1,padx=5,pady=5)
mainloop()

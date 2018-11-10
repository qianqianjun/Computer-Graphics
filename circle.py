"""
write by 高谦
"""
import turtle as tu
from tkinter import *
root=Tk()
root.title("画圆程序")
#使用turtle画圆函数：
def show():
    r=int(e1.get())
    e1.delete(0,END)
    tu.screensize(1080,720)
    tu.setup(startx=None,starty=None)
    tu.pencolor("red")
    tu.penup()
    tu.goto(0,20)
    tu.pendown()
    d=1.25-r
    x=0
    y=r
    add=1
    def move(x,y):
        tu.penup()
        tu.goto(x,y)
        tu.pendown()
        tu.goto(x+add,y+add)
    def draw(x,y):
        move(x,y)
        move(-x,-y)
        move(-x,y)
        move(y,x)
        move(x,-y)
        move(-y,-x)
        move(-y,x)
        move(y,-x)
        tu.penup()
        tu.goto(x,y)
        tu.pendown()
    while x<=y :
        if d<0 :
            d+=2*x+3;
        else :
            d+=2*(x-y)+5
            y-=1
        x+=1
        draw(x,y)
    tu.mainloop()
Label(root,text="输入圆的半径").grid(row=0,column=0,padx=0,pady=5)
e1=Entry(root)
e1.grid(row=0,column=1,padx=5,pady=5)
Button(root,text="开始画圆",command=show).grid(row=1,column=0,padx=0,pady=5)
Button(root,text="退出程序",command=root.quit).grid(row=1,column=1,padx=5,pady=5)
mainloop()
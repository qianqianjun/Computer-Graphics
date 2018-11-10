"""
write by 高谦
"""
import turtle
import math
from tkinter import *
def run():
    turtle.screensize(1920,1080)
    turtle.penup()
    point=[]
    temp = [int(x1.get()), int(y1.get())]
    point.append(temp)
    temp = [int(x2.get()), int(y2.get())]
    point.append(temp)
    temp = [int(x3.get()), int(y3.get())]
    point.append(temp)
    temp = [int(x4.get()), int(y4.get())]
    point.append(temp)
    temp = [int(x5.get()), int(y5.get())]
    point.append(temp)
    temp = [int(x6.get()), int(y6.get())]
    point.append(temp)
    #画出原图：
    for i in point:
        turtle.goto(i[0],i[1])
        turtle.pendown()
    turtle.goto(point[0][0],point[0][1])
    #画出旋转后的图片：
    newpoints=[]
    pointx=1
    pointy=1
    pointrotate=math.pi/6
    for i in point:
        # length=math.sqrt((i[0]-pointx)**2+(i[1]-pointy)**2)
        # rotate=pointrotate+math.atan((i[1]-pointy)/(i[0]-pointx))
        # temp=[length*math.cos(rotate)+pointx,length*math.sin(rotate)+pointy]
        temp=[i[0]*math.cos(pointrotate)-i[1]*math.sin(pointrotate),i[0]*math.sin(pointrotate)+i[1]*math.cos(pointrotate)]
        newpoints.append(temp)
    turtle.penup()
    for i in newpoints:
        turtle.goto(i[0],i[1])
        turtle.pendown()
    turtle.goto(newpoints[0][0],newpoints[0][1])
    turtle.penup()
    turtle.mainloop()
tk=Tk()
tk.title("多边形旋转算法:")
Label(tk,text="请输入六个顶点:").grid(row=0)
Label(tk,text="1:").grid(row=1)
Label(tk,text="2:").grid(row=2)
Label(tk,text="3:").grid(row=3)
Label(tk,text="4:").grid(row=4)
Label(tk,text="5:").grid(row=5)
Label(tk,text="6:").grid(row=6)
x1=Entry(tk)
x2=Entry(tk)
x3=Entry(tk)
x4=Entry(tk)
x5=Entry(tk)
x6=Entry(tk)
x1.grid(row=1,column=1)
x2.grid(row=2,column=1)
x3.grid(row=3,column=1)
x4.grid(row=4,column=1)
x5.grid(row=5,column=1)
x6.grid(row=6,column=1)

y1=Entry(tk)
y2=Entry(tk)
y3=Entry(tk)
y4=Entry(tk)
y5=Entry(tk)
y6=Entry(tk)
y1.grid(row=1,column=2,padx=3,pady=2)
y2.grid(row=2,column=2,padx=3,pady=2)
y3.grid(row=3,column=2,padx=3,pady=2)
y4.grid(row=4,column=2,padx=3,pady=2)
y5.grid(row=5,column=2,padx=3,pady=2)
y6.grid(row=6,column=2,padx=3,pady=2)
Button(tk,text="开始旋转",width=10,command=run).grid(row=7,column=0)
Button(tk,text="退出程序",width=10,command=tk.quit).grid(row=7,column=1)
tk.mainloop()

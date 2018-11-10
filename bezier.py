"""
write by 高谦
"""
import turtle
from tkinter import *
def run():
    turtle.screensize(1920,1080)
    point=[]
    temp = [float(x1.get()), float(y1.get())]
    point.append(temp)
    temp = [float(x2.get()), float(y2.get())]
    point.append(temp)
    temp = [float(x3.get()), float(y3.get())]
    point.append(temp)
    temp = [float(x4.get()), float(y4.get())]
    point.append(temp)
    temp = [float(x5.get()), float(y5.get())]
    point.append(temp)
    temp = [float(x6.get()), float(y6.get())]
    point.append(temp)
    turtle.penup()
    turtle.pensize(2)
    for i in point:
        turtle.goto(i[0],i[1])
        turtle.pendown()
    turtle.goto(point[0][0],point[0][1])
    turtle.penup()
    turtle.goto(point[0][0],point[0][1])
    turtle.pendown()
    turtle.pensize(1)
    turtle.pencolor('red')
    T=0.001
    while T<1:
        B0=(1-T)**5
        B1=5*T*(1-T)**4
        B2=10*T**2*(1-T)**3
        B3=10*T**3*(1-T)**2
        B4=5*T**4*(1-T)**1
        B5=T**5
        x=B0*point[0][0]+B1*point[1][0]+B2*point[2][0]+B3*point[3][0]+B4*point[4][0]+B5*point[5][0]
        y=B0*point[0][1]+B1*point[1][1]+B2*point[2][1]+B3*point[3][1]+B4*point[4][1]+B5*point[5][1]
        turtle.goto(x,y)
        T+=0.001
    turtle.mainloop()
tk=Tk()
tk.title("输出贝塞尔曲线: power by 高谦")
Label(tk,text="输入顶点:").grid(row=0)
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
y1.grid(row=1,column=2,padx=5,pady=5)
y2.grid(row=2,column=2,padx=5,pady=5)
y3.grid(row=3,column=2,padx=5,pady=5)
y4.grid(row=4,column=2,padx=5,pady=5)
y5.grid(row=5,column=2,padx=5,pady=5)
y6.grid(row=6,column=2,padx=5,pady=5)
Button(tk,text="开始绘制",width=10,command=run).grid(row=7,column=1,pady=5)
Button(tk,text="退出程序",width=10,command=tk.quit).grid(row=7,column=2,pady=5)
tk.mainloop()

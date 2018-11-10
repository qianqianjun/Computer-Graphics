"""
write by 高谦
"""
import turtle
import math
from tkinter import *
#活性边表节点：
class AetNode(object):
    def __init__(self,x,tx,my):
        self.x=x
        self.tx=tx
        self.my=my
    def op(self):
        return self.x
class AetList(object):
    def __init__(self,y):
        self.y=y
        self.numy=0
        self.l=[]
        pass
def findRange(point):
    # 找到最大y和最小y：
    maxy = point[0][1]
    miny = point[0][1]
    for i in point:
        if maxy < i[1]:
            maxy = i[1]
        if miny > i[1]:
            miny = i[1]
    return (miny,maxy)
def printNewEegeList(newEdgeTable):
    print("新边表是：")
    for i in newEdgeTable:
        print(i.y)
        for j in i.l:
            print((j.x,j.tx,j.my))
        print("__________________________________")
def createNewEdgeTable(point):
    miny,maxy=findRange(point)
    # 找打所有y的顶点：
    Y = []
    for i in point:
        Y.append(i[1])
    Y = set(Y)
    Y = list(Y)
    # 创建新边表:
    newEdgeList = []
    y=miny
    while y <=maxy:
        if y in Y:
            # 找到所有的X值：
            print(y)
            templist=[]
            for i in range(0, 6):
                if point[i][1] == y:
                    templist.append(i)
            print(templist)
            print("一次创建新边表")
            lists = AetList(y)
            for temp in templist:
                index1 = (temp + 7) % 6
                index2 = (temp + 5) % 6
                print(point[temp][0],point[temp][1])
                print(point[index1][0],point[index1][1])
                print(point[index2][0],point[index2][1])
                print("+++++++++++++++++++++")
                # lists = AetList(y)
                if point[index1][1] > y:
                    lists.numy+=1
                    if point[index1][1] - point[temp][1]==0:
                        node = AetNode(point[temp][0],0,point[index1][1])
                    else:
                        node = AetNode(point[temp][0],
                                   ((point[index1][0] - point[temp][0]) / (point[index1][1] - point[temp][1])),
                                   point[index1][1])
                    lists.l.append(node)
                if point[index2][1] > y:
                    lists.numy+=1
                    if point[index2][1] - point[temp][1]==0:
                        node = AetNode(point[temp][0], 0, point[index2][1])
                    else:
                        node = AetNode(point[temp][0],
                                       ((point[index2][0] - point[temp][0]) / (point[index2][1] - point[temp][1])),
                                       point[index2][1])
                    lists.l.append(node)
            if len(lists.l)!=0:
                lists.l.sort(key=AetNode.op)
                if len(templist)>1:
                    lists.numy-=1
                newEdgeList.append(lists)
        y+=1
    printNewEegeList(newEdgeList)
    return (newEdgeList,Y)
def draw(x1,y1,x,y):
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x,y)
def run():
    turtle.screensize(1920,1080)
    turtle.penup()
    turtle.hideturtle()
    point=[]
    # point=[[20,20],[50,10],[110,30],[110,80],[50,50],[20,70]]
    # point=[[-10,-10],[10,-10],[15,0],[10,10],[-10,10],[-15,0]]
    temp = [float(x11.get()), float(y1.get())]
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
    point = [[20, 20], [50, 10], [110, 30], [110, 80], [50, 50], [20, 70]]
    #画出原图：
    for i in point:
        turtle.goto(i[0],i[1])
        turtle.pendown()
    turtle.goto(point[0][0],point[0][1])
    #创建新边表：
    newEdgeTable,Y=createNewEdgeTable(point)
    miny,maxy=findRange(point)
    y=miny
    acativeList=[]
    while y<=maxy:
        #把新边表加进来：
        ynum=0
        if y in Y:
            for i in newEdgeTable:
                if i.y==y:
                    for j in i.l:
                        acativeList.append(j)
                    ynum=i.numy
                    break
            acativeList.sort(key=AetNode.op)
            for j in acativeList:
                print((j.x,j.tx,j.my))
            print("****************")
        #进行填色：
        i=0
        flag=True
        while i<len(acativeList)-1:
            x1=acativeList[i].x
            temp=[acativeList[i+1].x,y]
            if temp in point and ynum>=1:
                ynum-=1
            else:
                i+=1
            if flag:
                draw(x1,y,temp[0],y)
            flag=not flag
        #更新活性边表：
        newacativeList=[]
        for i in acativeList:
            if i.my>y:
                i.x+=i.tx
                newacativeList.append(i)
        acativeList=newacativeList
        y+=1
    turtle.mainloop()
tk=Tk()
tk.title("扫描填充算法:by 高谦")
Label(tk,text="输入顶点:").grid(row=0)
Label(tk,text="1:").grid(row=1)
Label(tk,text="2:").grid(row=2)
Label(tk,text="3:").grid(row=3)
Label(tk,text="4:").grid(row=4)
Label(tk,text="5:").grid(row=5)
Label(tk,text="6:").grid(row=6)
Label(tk,text="例:\n\n").grid(row=9)
Label(tk,text="(20,20),(50,10)\n(110,30),(110,80)\n(50,50),(20,70)").grid(row=9,column=1)
Label(tk,text="(-10,-10),(10,-10)\n(15,0),(10,10)\n(-10,10),(-15,0)").grid(row=9,column=2)
x11=Entry(tk)
x2=Entry(tk)
x3=Entry(tk)
x4=Entry(tk)
x5=Entry(tk)
x6=Entry(tk)
x11.grid(row=1,column=1)
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
Button(tk,text="扫描填充",width=10,command=run).grid(row=7,column=1)
Button(tk,text="退出程序",width=10,command=tk.quit).grid(row=7,column=2)
tk.mainloop()

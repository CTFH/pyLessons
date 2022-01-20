import random 
import turtle
ts=[]
#画面の真ん中が00　画面幅1290　645が画面の端
def setup():
    global ts
    startline=-620
    screen=turtle.Screen()
    screen.setup(1290,720)#720縦
    screen.bgpic('pavement.gif') #bgpic backgroundpic

    t_y=[-40,-20,0,20,40]
    t_color=['blue','red','purple','brown','green']

    for i in range(len(t_y)):
        t=turtle.Turtle()
        t.shape('turtle')
        t.penup()
        t.setpos(startline,t_y[i])
        t.color(t_color[i])
        t.pendown()
        ts.append(t)

def race():
    global ts
    finishline=590

    while True:
        for current_t in ts:
            move=random.randint(0,10)
            current_t.forward(move)

            x=current_t.xcor() #現在のx座標
            if x >=finishline:
                winner_color=current_t.color()
                current_t.write('Win!'+winner_color[0],font=('Arial',16,'normal'))
                break
        else:
            continue
        break

setup()
race()
turtle.mainloop()

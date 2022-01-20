kame1
import turtle
t=turtle.Turtle() # インスタンス作成
t.shape('turtle') # 見た目を亀に
t.circle(100) # 半径100の円を描画
turtle.mainloop() # 実行を監視


kame2
import turtle
t=turtle.Turtle() # インスタンス作成
t.shape('turtle') # 見た目を亀に
t.forward(100)#向いている方向に100移動
t.right(90) # 90度右回転
t.forward(100)
t.home()#原点に移動し、デフォルトの方向を向く（右）
turtle.mainloop() # 実行を監視



kame3
import turtle
t=turtle.Turtle() # インスタンス作成
t.shape('turtle') # 見た目を亀に
for i in range(4):
    t.forward(100)#向いている方向に100移動
    t.right(90) # 90度右回転
t.home()#原点に移動し、デフォルトの方向を向く（右）
turtle.mainloop() # 実行を監視



kame4
import turtle
t=turtle.Turtle() # インスタンス作成
t.shape('turtle') # 見た目を亀に
for i in range(5):
    t.forward(100)#向いている方向に100移動
    t.right(144) # 90度右回転
t.home()#原点に移動し、デフォルトの方向を向く（右）
turtle.mainloop() # 実行を監視



kame5
import turtle
t=turtle.Turtle() # インスタンス作成
t.shape('turtle') # 見た目を亀に
t.color('blue')#線を青色に
t.forward(100)#向いている方向に100移動
t.left(90) # 90度右回転
t.forward(100)
t.right(90)
f.forward(100)
t.penup()#ペンを持ち上げる（線が描画されない）
t.home()#原点に移動し、デフォルトの方向を向く（右）

turtle.mainloop() # 実行を監視



kame6
import turtle
t1=turtle.Turtle() # インスタンス作成
t1.shape('turtle') # 見た目を亀に
t1.color('blue')#線を青色に
t2=turtle.Turtle()
t2.shape('turtle')
t2.color('red')

def make_square(t1,t2):
    for i in range(4):
        t1.forward(100)#向いている方向に100移動
        t1.right(90)
        t2.forward(100)
        t2.right(90)

def make_spiral(t1,t2):
    for i in range(36):
        make_square(t1,t2)
        t1.right(10)
        t2.right(10)

t2.right(5)
make_spiral(t1,t2)

turtle.mainloop() # 実行を監視



turtleRace
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
        else: #途中で抜けたらelse通らず、その下のbreak
            continue #loopの上（条件式）に行く
        break

setup()
race()
turtle.mainloop()

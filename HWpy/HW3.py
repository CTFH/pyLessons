import random
import turtle
import json

json_file = open("HW2.json", "r",encoding="utf-8")
json_obj = json.load(json_file)
print(json_obj)

ans=[]
for i in range(3):
    ids=random.randint(0,10)
    n=int(input(json_obj[ids]))
    
    ans[3]=int(input('レースで勝つのは何色の亀?'))





ans=[]
for i in range(3):
    ids=random.randint(0,10)
    n=int(input(data[ids]))
    if dataA[ids]==n:
        ans.append(True)
    else:
        ans.append(False)


t=turtle.Turtle()
t.shape('turtle')
t.color('blue')

def setup():
    startline=-300
    screen=turtle.Screen()
    screen.setup(800,500)
    t.penup()
    t.setpos(-300,0)
    t.pendown()

right=0

def race():
    finishline=200

    for k in range(3):
        move = 100
        if ans[k]==True:
            t.forward(move)
            global right
            right +=1
            
    x=t.xcor()
    if x ==finishline:
        t.write('Gold medal!!',font=('Arial',26,'normal'))
    if x ==-100:
        t.write('Silver medal!',font=('Arial',26,'normal'))
    if x ==-200:
        t.write('Bronze medal!',font=('Arial',26,'normal'))
        


setup()
race()

if right == 0:
    print('ぼちぼち行こう')
elif right == 1:
    print('銅メダル')
elif right==2:
    print('銀メダル')
else :
    print('金メダル')

turtle.mainloop()
import requests as req
import json
import turtle as tt
URL='http://api.open-notify.org/iss-now.json'
screen=None; #初期化
iss=None; #初期化（いきなり1行書いておくわけにいかないから）

def setup():
    global iss,screen
    screen=tt.Screen()#g画面を作る際にタートルモジュールのスクリーンメソッドを使用する
    screen.setup(1000,500)
    screen.bgpic('earth.gif')
    #座標系を変換
    screen.setworldcoordinates(-180,-90,180,90)
    tt.register_shape('iss.gif')#※画像を登録
    iss=tt.Turtle()#インスタンス作成
    iss.shape('iss.gif')#見た目を変換 画像を登録と見た目を変換の2行にしないとできない
    iss.pencolor('red')
    iss.hideturtle() #最初隠しておいて現在地のところから始めるため
    iss.penup()

def track_iss():
    res=req.get(URL)
    data=json.loads(res.text)
    pos=data['iss_position']
    lat=float(pos['latitude'])
    lng=float(pos['longitude'])
    print('緯度{},経度{}'.format(lat,lng))
    iss.goto(lng,lat)
    if not iss.isvisible(): #最初隠れているからTrue
        iss.pendown()
        iss.showturtle()#所定の位置に来たら見えるようにする

    canvas=tt.getcanvas() #下に同じ
    canvas.after(5000,track_iss)#5秒ごとに描画を更新するのにこれが必要
    #track_issという関数を呼び出している

setup()
track_iss()
tt.mainloop()

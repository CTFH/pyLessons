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


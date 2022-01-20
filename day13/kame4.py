import turtle
t=turtle.Turtle() # インスタンス作成
t.shape('turtle') # 見た目を亀に
for i in range(5):
    t.forward(100)#向いている方向に100移動
    t.right(144) # 90度右回転
t.home()#原点に移動し、デフォルトの方向を向く（右）
turtle.mainloop() # 実行を監視


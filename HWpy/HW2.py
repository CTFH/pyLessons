import random
import turtle

data=[
    '2022年冬季オリンピックの開催地は？\n1.パリ, 2.北京, 3.ロンドン',
    '2024年夏季オリンピックの開催地は？\n1.パリ, 2.北京, 3.ロンドン',
    '2021年東京オリンピック柔道100キロ級男子の金メダリストは？\n1.ワルフ・アロン,2.ウルフ・アローン,3.ウルフ・アロン',
    '2021年東京オリンピック柔道女子で兄妹で金メダルをとった妹の名前は？\n1.阿部詩,2.阿部唄,3.阿部一二三',
    '2022年冬季オリンピックフィギュアスケート女子で4回転を飛べる金メダル候補と言われている選手は？\n1.カミラ夫人,2カミーラ・ワリエワ.,3.カミラ・ワリエワ,',
    '2022年冬季オリンピックフィギュアスケート男子代表の羽生結弦選手が目指しているジャンプの種類は？\n1.トリプルアクセル,2.クワドラプルアクセル,3.クワドラプルルッツ',
    '元オリンピック男子体操2連覇金メダリストで2022年に引退会見を行った選手は？\n1.橋本大輝,2.内村航平,3.萱 和磨',
    '癌との闘病生活に打ち勝ち女子競泳選手として2021年東京オリンピックに代表として参戦した選手は？\n1.池江璃花子,2.池本里香,3.池内理香子',
    '2022年東京オリンピック初種目で四十住さくら選手が金メダルを取得した種目は？\n1.スケッチボード女子パーク,2.スケートボード女子パーク,3.スポーツクライミング女子',
    '2021年東京オリンピックで初採用種目となったのはスケートボード、サーフィンとあと１つは？\n1.ロッククライミング,2.ウォールクライミング,3.スポーツクライミング',
    '2024年パリオリンピックで初採用種目となったのは？\n1.ブレイクダンス,2.ヒップホップ,3.バレエ',
    ]

dataA=[2,1,3,1,3,2,2,1,2,3,1]


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
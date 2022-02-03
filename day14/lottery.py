import random 

lotts = ['{:04d}'.format(i) for i in range(10000)]
#04d...0埋めした4桁の数字 足りない桁は0埋めしてくれる
#「:」が書式設定 dはdicimal
#(テストにはでない)
#文字列だから「’’」も出力される
#配列だから「,」も出力される

'''
print('{}の２倍は{}'.format(10,20))
print(f'{10:04d}の２倍は{20:04d}')
print(f'{3.141592:.2f}の２倍は{20:04d}')
.formatはテストに出るかも
'''

#print(lotts)

n=int(input('宝くじを何枚買いますか?>>'))
my_lotts=sorted(random.sample(lotts,n))
'''
random.sample(リスト,個数)
リストから指定個数分,重複なしに要素を取得しそれを
構成要素としたリストを返してくれる。
10000個のくじの中から重複なしに５個を選ぶ
l=sorted(リスト)
とすることで昇順に並び替えたリストを新たに作成し返却する。
（sortedは元を保持したまま新しいリストを返却。sortは元をぶっ壊す）
降順に並べるときはreverse=True
my_lotts=sorted(random.sample(lotts,n),revedrse=True)
'''
print(my_lotts)

---
n1 = random.randint(1,6) #1~6
n2 = random.randrange(2,10) #2~9
#randrange(0,100,2) 0~99で２おき 0,2,4
#randrange(100) 0~99
data = ['red', 'green','blue']
color=random.choice(data) #チョイスは１つだけ選ぶ(戻り値配列じゃない)
#スライスのエンドは含まない
#Random.Range(1,7) unity 後ろ含まない

random.shuffle(data)
#shuffleは戻り値の型ないNoneが戻り値の型のようなもの
#shuttleは型壊しちゃう
---


lucky='{:04d}'.format(random.randrange(10000))
print('抽選開始...')
for c in lucky:
    time.sleep(1)
    print(c)
'''
pythonは文字列をそのままfor文にかけることができる。
その場合、一文字ずつループで取り出す。
print(lucky[0])#先頭の文字
'''
result=[[]for i in range(4)]#４つ空っぽの配列がある２次元配列ができる
#[[],[],[],[]]
for lott in my_lotts:
    if lucky == lott:
        result[0].append(lott)
    elif lucky[-3:]==lott[-3:]: #下３桁が等しいか
        result[1].append(lott)
    elif lucky[-2:]==lott[-2:]: #下２桁が等しいか
        result[2].append(lott)
    elif lucky[-1]==lott[-1]:
        result[3].append(lott)

for i in range(len(result)):
    print('{}等賞（{:*>4s}）'.format(i+1,lucky[i:]),result[i])
#「*」足りない桁、「>」右詰め、４桁の文字列。
#len(result)=4
#「<」左詰め、「^」センタリング
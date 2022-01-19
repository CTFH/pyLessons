"""0-9の乱数を10個生成する
その中にもし7があれば最初に登場したindexを表示
なければありませんでしたと表示する処理を作成せよ

[実行例]
[4,1,0,5,7,7,2,..]
index4に7はありました

[4,1,0,5,1,2,3,1,4,5]
7はありませんでした"""

import random
list = []
for i in range(10):
    n=random.randint(0,9)
    list.append(n)

print(list)
for j in range(10):
    if list[j]==7:
        print(f'index{j}に7はありました')
        break
else:
    print('7はありませんでした')

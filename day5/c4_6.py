scores =[80,20,75,60]
count=0
while count < len(scores): #リストの要素数より小さければ繰り返す
    if scores[count]>=60: #添え字にカウンタ変数を使用
        print('合格')
    else:
        print('不合格')
    count += 1

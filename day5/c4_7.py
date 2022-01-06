scores =[80,20,75,60]
#for(int data : scores){}
for data in scores: #リストの要素数より小さければ繰り返す
    if data>=60: #添え字にカウンタ変数を使用
        print('合格')
    else:
        print('不合格')

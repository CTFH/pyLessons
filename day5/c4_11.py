ages=[28,50,'ひみつ',20,78,25,22,10,'無回答',33]
samples=list()
for data in ages:
    #if (! data instanceof Integer){}
    if not isinstance(data, int): #整数でないデータはスキップ
        #isinstance(データ、データ型）
        #データがデータ型と一致したらTrueに置き換わる
        continue
    if data < 20 or data >= 30:
        continue
    
    samples.append(data)
print(samples)

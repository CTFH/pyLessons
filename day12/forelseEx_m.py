import random
data=[random.randint(0,9) for i in range(10)]
#random.randrange(1,10,2)で奇数が出てくる
print(data)
for i in range(len(data)):
    if data[i]==7:
        print(f'index{i}に7はありました')
        break
else:
    print('7はありませんでした')


import random
data=[random.randint(0,9) for i in range(10)]
print(data)
if 7 in data:
    print(f'index{data.index(7)}に７はありました')
else:
    print('7はありませんでした')

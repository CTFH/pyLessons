import pprint
data=list()
for i in range(10):
    temp=list()
    for j in range(10):
        temp.append(0)
    data.append(temp)
print(data)

pprint.pprint(data)


W=10
H=10
data=[None]*H #空っぽの配列にはappendで追加していくしかない
                #要素数10個の配列がNoneでできるのでappendしなくてOK
                #deep copyなので１つ書き換えてもそこだけ書き変わる
for i in range(H):
    data[i]=[0]*W
pprint.pprint(data)


data2=[[0]*W]*H #shallow copyなので１つ書き換えると全て書き変わってしまう
pprint.pprint(data2)

data2[1][1]=5
pprint.pprint(data2)



data3=[[0]*W for i in range(H)]
pprint.pprint(data)


#ex
for i in range(H):
    temp=[None]*W
    for j in range(W):
        temp[j]=i*10+j+1
    data[i]=temp
pprint.pprint(data)

data5=[[i*10 + j for j in range(1,11)] for i in range(0,10)]
pprint.pprint(data)


#quita
x=[i for i in range(1, 8)]
print(x) #[1,2,3,4,5,6,7]

x=[i**2 for i in range(1,8)]
print(x) #[1,4,9....]

x=[i for i in range(1,8) if i % 2 == 0]
print(x) #[2,4,6]

x=[i for i in range(2,7,2)]
print(x) #[2,4,6]

x=[i*10+j  for i in range(1,3) for j in range(2,5) ]
print(x) #[12,13,14,22,23,24]

x=[[i*10 +j for j in range(7,10)]for i in range(1,3)]
print(x) #[[17,18,19,],[27,28,29]]

row=col=3
matrix=[[1 if i==j else 0 for j in range(col)]for i in range(row)]
print(x) #[[1,0,0],[0,1,0][0,0,1]]



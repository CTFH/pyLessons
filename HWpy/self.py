import random
members=['大迫','古橋','久保','堂安','南野','伊東','田中','遠藤','富安','吉田','長友','酒井']

random.shuffle(members)


length=int(len(members)/2)
lengthAll=int(len(members))

A=[]
B=[]
for i in range(length):
    A.append(members[i])

for j in range(lengthAll-length,lengthAll):
    B.append(members[j])


print('--チームA--')
print(f'reader:{A[0]}')
for i in range (len(A)):
    print(A[i])

print('--チームB--')
print(f'reader:{B[0]}')
for j in range (len(B)):
    print(B[j])

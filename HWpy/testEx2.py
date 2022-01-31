import random
members=['大迫','古橋','久保','堂安','南野','伊東','田中','遠藤','富安','吉田','長友','酒井']

random.shuffle(members)

teamNum=int(input('いくつチームを作りますか(1-12)?'))

length=int(len(members)/teamNum)
#if len(members)%teamNum!=0:
 #   len(members)//teamNum



A=[]
for i in range(length):
    A.append(members[i])


print('--チームA--')
print(f'reader:{A[0]}')
for i in range (len(A)):
    print(A[i])



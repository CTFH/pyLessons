import random
import string

members=['大迫','古橋','久保','堂安','南野','伊東','田中','遠藤','富安','吉田','長友','酒井']

random.shuffle(members)

#def listAlphabet():
#    return list(string.ascii_uppercase)


teamNum=int(input('いくつチームを作りますか(1-12)?'))

alph=[A,B,C,D,E,F,G,H,I,J,K,L]
for i in range teamNum:
    list(alph[i]) = []

#teamPpl=len(members)//teamNum
#teamPplEx=len(members)%teamNum

for i in range (len(members)):
    list(alph[i])=members[i]

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



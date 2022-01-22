import random
import json

json_file=open('HW.json', 'r')
json_object=json.load(json_file)

ans=[]
for i in range(3):
    ans[i]=input(json_object[random.randint(1,11)])
    ans[3]=int(input('レースで勝つのは何色の亀?'))

right=0
if q1==ans[0]: 
    right +=1
if q2==ans[1]:
    right +=1
if q3==:
    right +=1

if right == 0:
    print('ぼちぼち行こう')
elif right == 1:
    print('銅メダル')
elif right==2:
    print('銀メダル')
else :
    print('金メダル')
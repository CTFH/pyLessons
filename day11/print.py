c7_1
text=input('何を記録しますか？>>')
file=open('diary.txt', 'a')
file.write(text + '\n')
file.close()


c7_2
text=input('今日は何をした？>>')
with open('diary.txt', 'a', encoding='utf-8') as file:
    file.write(text + '\n')


c7_3
import math 
print('円周率は{}です'.format(math.pi))
print('小数点以下を切り捨てれば{}です'.format(math.floor(math.pi)))
print('小数点以下を切り上げれば{}です'.format(math.ceil(math.pi)))


7_4
import math as m 
print('円周率は{}です'.format(m.pi))
print('小数点以下を切り捨てれば{}です'.format(m.floor(m.pi)))
print('小数点以下を切り上げれば{}です'.format(m.ceil(m.pi)))


c7_5
from math import pi 
from math import floor 
print('円周率は{}です'.format(pi))
print('小数点以下を切り捨てれば{}です'.format(floor(pi)))


c7_7
from math import pi as ensyuritsu 
from math import floor as kirisute
print('円周率は{}です'.format(ensyuritsu))
print('小数点以下を切り捨てれば{}です'.format(kirisute(ensyuritsu)))


c7_12
import matplotlib.pyplot as plt
weight=[68.4,
        68.0, 
        69.5, 
        68.4, 
        68.6, 
        70.2, 
        71.4, 
        70.8,
        68.5, 
        68.6, 
        68.3, 
        68.4]
plt.plot(weight)
plt.show()



c7_13
import requests
response = requests.get('https://www.python.org/downloads/')
text=response.text
print(text)


self
from math import pi
pi=3
print(pi) #3


ex7_5
file=open('sample.txt', 'r')
for line in file:
    print(line)
file.close()

file_r=open('sample.txt', 'r')
file_w=open('copy.txt', 'w')
for line in file_r:
    file_w.write(line)
file_r.close()
file_w.close()



ex1
#コピー元のファイルパスとコピー後のファイルパスを入力>>
#file1.txt, file1copy.tx
orgName,cpName=input('コピー元のファイルパスとコピー後のファイルパスをお入力>>').split(',')
with open(orgName,'r',encoding='utf-8')as reader, open(cpName, 'w',encoding='utf-8')as writer:
    for line in reader:
        writer.write(line)

ex7_6
import random
print('数あてゲームを始めます。３桁の数を当ててください！')
answer=[random.randint(0,9) for i in range(3)]
#randint(0,9) → 0~9

while(True):
    prediction=[int(input(f'{i}桁目の予想を入力(0~9)>>'))for i in range(1,4)]

#print(answer)
#print(prediction)
    
    hit=ball=0
    for i in range(len(prediction)):
        if answer[i]==prediction[i]:
            hit+=1
        else:    
            for j in range(len(answer)):
                if answer[i]==prediction[j] and i!=j:
                    ball+=1
                    break
        #else:
        #if prediction[i] in answer:
            #ball +=1
    
    print(f'{hit}ヒット、{ball}ボール')
    if hit==len(answer):
        print('正解')
        break
    else:
        if int(input('続けますか？ 1:続ける 2:終了 >>'))==2:
                print(f'正解は{answer[0]}{answer[1]}{answer[2]}でした')
                break

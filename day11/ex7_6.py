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
        if int(input('続けますか？ 1:続ける 2:終了 >>'))!=1:
                print(f'正解は{answer[0]}{answer[1]}{answer[2]}でした')
                break

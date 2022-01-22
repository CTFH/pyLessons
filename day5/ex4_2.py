count=1
#ans = True
print('カレーを召し上がれ')
while True: #while ans == True:
    print(f'{count}皿のカレーを食べました')
    key = input('おかわりはいかがですか？(y/n)>>')
    if key == 'y':
        count +=1
    else:
        #ans = False
        print('ごちそうさまでした') #printが左
        break #breakなし

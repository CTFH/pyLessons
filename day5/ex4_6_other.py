numbers=[1,1]
while True: #回す回数の検討がつかないのでwhile True
    n=numbers[-2]+numbers[-1]
    if n>=1000:
        break
    numbers.append(n)
print(numbers)

ratios=[]
for i in range(1, len(numbers)): #1から始まってlen(numbers)未満
                                #0から始めると一個前と比較できない
    ratios.append(numbers[i]/numbers[i-1])
print(ratios)

for i in range(len(ratios)):
    ratios[i]=int(ratios[i] * 1000)/1000
print(ratios)

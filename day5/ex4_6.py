numbers = [1,1]
data = sum(numbers) #最初に追加する値を算出
count=2 #indexのこと
while data <=1000:
    numbers.append(data)
    data= data +numbers[count-1] #次に追加する値は、今追加した値と
                                    #１つ前の値との合計
    count +=1
print(numbers)


ratios = list()
for count in range(len(numbers)):
    if count == len(numbers)-1:
        break
    ratios.append(numbers[count+1]/numbers[count])
print(ratios)

for count in range(len(ratios)):
    ratios[count]=int(ratios[count]*1000)/1000
print(ratios)


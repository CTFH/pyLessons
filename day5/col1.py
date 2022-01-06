import random
n= random.randint(1,10)
#let div = n %2==0? "偶数":"奇数";
div ='偶数' if n%2==0 else '奇数'
print(f'{n}は{div}です')

result='優' if n>=9 else '良' if n>=6 else'可' if n>=3 else '不可'
print(result)

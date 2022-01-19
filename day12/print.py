cb_1


def funcA(z):
    ans=z*a #error a not defined
    print(ans)


def funcB(x,y):
    z=x+y
    funcA(z)

x=10
y=20
funcB(10,20)


print('hello) '#SyntaxError: EOL while scanning string literal
        #EOL=end of line
        #EOF=end of file

my_list=[10,20,30  #SyntacError: unexpected EOF while parsing


x=10
if(x<10):
    print('hoge')
else:  #SyntaxError: unexpected EOF while parsing



x=10
if(x<10):
    print('hoge')
else: 
print('hoo')  #IndentationError: expected an indented block



x　= 10 #全角スペース
#SyntaxError: invalid charcter in identifier


print(hello）#全角丸カッコ
    #SyntaxError: invalid character in identifier

#実行時エラー
print(x) #定義してない変数ｘを使用  NameError: name'x' is not difined


x=10
print('hello' + x)
#TypeError: can only concatenate str(not 'int') to str
#文字列helloと数字10を連結した


print('hello' **5)
#TypeError unsupported operand type** or pow(): 'str' and 'int'


def hello():
    print('Hello')
    hello('World')
#仮引数がないhello関数に、実引数１つ指定した
#TypeError: hello() takes 0 positional arguments but 1 was given


x=10
y=0
ans=x/y #10を0で割った
#ZeroDivisionError: division by zero


x='hello'
x=int(x)
#ValueError: invalid literal for int() with base10: 'hello'
#int関数に整数に変換できない値を代入


a=100
def=hoge():
    print(a)
    a=10
hoge() #a=10が無ければＯＫ　でもあるので
#UnboundLocalError: local variable 'a' referenced before assignment
#変数aの値を参照した後に初期化を行った
#global がついていればＯＫ
#★★★


a=100
def hoge():
    global a
    print(a)
    a=10
hoge()
print(a) #10
#globalが入っているのでhoge呼び出した時点の中では100
#そのあとaに10代入しているので最後のprint(a)で10



#attribute属性
import math
math.power(10,2)
#AttributeError: module 'math' has no attribute 'power'
#pow関数を呼び出すつもりで誤ってpowerと記述


x=0
while x<10:
    print('Hello')
#無限ループctrl + cで止める　★★★
#KeyboardInterrupt  無限ループを手動で止めた



try:
    print(int(input('料金を入力')))
    print(int(input('人数を入力')))
    print('1人あたり{}円です'.format(price/number))
except ValueError:
    print('料金または人数は整数を入力してください')
except ZeroDivisionError:
    print('人数に0は入力しないで下さい')
print('プログラムを終了します')



try:
    print(int(input('料金を入力')))
    print(int(input('人数を入力')))
    print('1人あたり{}円です'.format(price/number))
except:
    print('料金と人数に適切な整数を入力してください')
print('プログラムを終了します')



try:
    price=print(int(input('料金を入力')))
    number=print(int(input('人数を入力')))
    print('1人あたり{}円です'.format(price/number))
except:
    print('料金と人数に適切な整数を入力してください')
else:
    print('正常終了')
finally:
    print('ok')
print('プログラムを終了します')


my_dict={'hoge':1,'foo':2}
print(my_dict['foo'])



forelse
for i in range(10):
    #if i==7
    #break  　→完了が出ない
    print(i)
else:
    print('完了')
    #回り切ったときにelseが実行される



forelseEx_m
import random
data=[random.randint(0,9) for i in range(10)]
#random.randrange(1,10,2)で奇数が出てくる
print(data)
for i in range(len(data)):
    if data[i]==7:
        print(f'index{i}に7はありました')
        break
else:
    print('7はありませんでした')


import random
data=[random.randint(0,9) for i in range(10)]
print(data)
if 7 in data:
    print(f'index{data.index(7)}に７はありました')
else:
    print('7はありませんでした')


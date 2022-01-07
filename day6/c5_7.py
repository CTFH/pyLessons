def hello(name):
    print('こんにちは。{}です。'.format(name))
hello('浅木')
hello('松田')

def profile(name, age, hobby):
    print('私の名前は{}です。'.format(name))
    print('年齢は{}歳です。'.format(age))
    print('趣味は{}です。'.format(hobby))

profile('浅木',24,'カフェ巡り')

def plus(x,y):
    answer=x+y
    return answer
answer = plus(100,50)
print('足し算の結果は{}です'.format(answer))

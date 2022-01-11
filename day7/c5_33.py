name = '松田'
def change_name():
    global name
    name = '浅木'
def hello():
    print('こんにちは'+name+'さん')

change_name()
hello()　#浅木

name = '松田'
def change_name():
    global name
    name = '浅木'
    
def hello():
    print('こんにちは'+name+'さん')

hello() #松田（change_nameを実行してないから）

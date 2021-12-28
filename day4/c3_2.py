name = input('名前>>')
print('{}さん、こんにちは'.format(name))
food=input('{}さんの好きな食べ物>>'.format(name))
if food=='カレー':
    print('素敵です')
else:
    print('私も{}が好きです'.format(food))

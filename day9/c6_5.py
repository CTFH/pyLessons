class Hero:
    def __init__(self,name,hp): #constructor  
    #引数にselfが入ってくる　使うときには引数にself書かなくてOK
    #overload  同じメソッドの引数の数の違い
    #pythonはoverloadできない（でもデフォルト引数のがあるからオーバーロード不必要（朝食夕食のカレーのメソッド））
    #override  親クラスにあるメソッドを再定義すること
        self.name=name
        self.hp=hp
        name = '松田'
        hp = 100
    def sleep(self, hours): #第一引数に明示的に記載　呼び出すときにはいらない
        print('{}は{}時間寝た！'.format(self.name,hours))
        self.hp += hours

#ゲーム開始
print('スッキリファンタジーXII ~金色の理想郷~')
h = Hero('松田',100)
h.sleep(3)
print('{}のHPは現在{}です'.format(h.name, h.hp))



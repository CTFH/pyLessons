class Pencil:
    def __init__(self,color,length):
        self.color=color
        self.length=length

    def write(self):
        if self.length > 0:
            self.length-=1
            print(f'{self.color}で書いた({self.length})')
        else:
            print('もう書けません')

redPen = Pencil('赤', 5)
bluePen = Pencil('青', 5)

redPen.write()
print(redPen.length)

for i in range(10):
    bluePen.write()
    if bluePen.length<=0:
        break
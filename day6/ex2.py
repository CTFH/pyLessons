#関数min_maxを作成せよ
#任意数の引数を受け取り、その数の中の最大と最小を返すメソッド
#必須引数を1つとすること

#maxN,minN = min_max(3,4,1,5,3)
#print(f'最大{maxN},最小{minN}')

def min_max(n,*nums):
    minN,maxN=n,n
    for d in nums:
        if d<minN:
            minN=d
        if d > maxN:
           maxN=d
    return minN, maxN

maxN,minN = min_max(3,4,1,5,3)
print(f'最大{maxN},最小{minN}')


def max_min(n,*args):
    ls=list(args) #タプルは足せないからリストに変換
    ls.append(n)
    return max(ls),min(ls)

maxN,minN = max_min(3,4,1,5,3)
print(f'最大{maxN},最小{minN}')
     

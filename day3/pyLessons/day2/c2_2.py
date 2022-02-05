members=['工藤', '松田','浅木']
print(members)
print(members[0])#工藤
print(len(members))#要素数3
members.append('山田')#要素の追加はappend(jsはpush)
print(members)#jsはpushで追加　javaのlistはadd
members[3]='山崎'#要素の書き換え
print(members)
members.remove('山崎')
print(members)
#members.remove(0)#できない
del members[0]#index指定での削除はdel文
print(members)

nums=[10,20,30]
print(sum(nums))#合計60

print (sum(nums)/len(nums))#平均20

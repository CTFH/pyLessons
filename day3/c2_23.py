scores = {'network':60, 'database':80, 'security':60}
members = ['松田','浅木','工藤']
print(tuple(members))#リストmembersをタプルに変換
print(list(scores))#scoresのキーをリストに変換して表示
print(set(scores.values()))#scoresの値をセットに変換

color_en=['red','green','blue']
color_ja=['赤','緑','青']
color=dict(zip(color_en.color_ja))
print(color)

def add_suffix(names):
    for i in range(len(names)):
        names[i] = names[i] + 'さん'
    return names

before_names = ['松田', '浅木', '工藤']
copied_names=before_names[:] #配列のコピー

after_names = add_suffix(copied_names)
print('さん付け後:'+after_names[0])
print('さん付け前:'+before_names[0])

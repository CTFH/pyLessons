import random
import string

members=['大迫','古橋','久保','堂安','南野','伊東','田中','遠藤','富安','吉田','長友','酒井']

random.shuffle(members)

#def listAlphabet():
#    return list(string.ascii_uppercase)


teamNum=int(input('いくつチームを作りますか(1-12)?'))

teamNames=string.ascii_uppercase

data=[{'teamName':'チーム'+str(teamNames[i]),
        'teamMembers':[],
        'teamReader':None}
        for i in range(teamNum)]

for i in range(len(members)):
    member=members[i]
    data[i%len(data)]['teamMembers'].append(member)
    if i<teamNum:
        data[i%len(data)]['teamReader']=member

for team in data:
    print(f"---{team['teamName']}---")
    print(f"reader:{team['teamReader']}")
    for name in team['teamMemebers']:
        print(name)
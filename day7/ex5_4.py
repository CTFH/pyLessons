def analyze_scores(sansu, kokugo, rika, syakai, eigo=None, *others):
    ls=[]
    ls.append(sansu)
    ls.append(kokugo)
    ls.append(rika)
    ls.append(syakai)
    ls.append(eigo)
    for s in others:
        ls.append(s)
    max_score=max(ls)
    min_score=min(ls)
    avg_score=sum(ls)/len(ls)
    return [max_score, min_score, avg_score]

result=analyze_scores(80,80,80,80,80,80,80,80)
print(result)
result=analyze_scores(80,80,80,80,80,80)
print(result)
result=analyze_scores(eigo=80,kokugo=20,rika=30,syakai=40,sansu=70)
print(result)
result=analyze_scores(1,2,3,4,5)
print(result)
[x,n,g]=analyze_scores(1,2,3,4,5)
print(x,n,g)

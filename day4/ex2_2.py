scores=[]
scores.append(int(input('国語の点数>>')))
scores.append(int(input('算数の点数>>')))
scores.append(int(input('理科の点数>>')))
scores.append(int(input('社会の点数>>')))
scores.append(int(input('英語の点数>>')))
#let li=[]; js
#li.push(10); js
#li.push(20); js
#let sum=0;
#for(let i=0; i<li.length; i++){
#   sum+=li[i];
#  }
#console.log('合計点${s},平均点${avg}')  jsでの書き方　テスト出る？
print(f'合計{sum(scores)}点/平均{sum(scores)/len(scores)}点')

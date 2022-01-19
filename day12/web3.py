import requests
from bs4 import BeautifulSoup

res=requests.get('https://joytas.net/kaba/')
res.encoding=res.apparent_encoding
#第1引数にhtml文字列,第2引数にパーサーを指定する。今回は追加ライブラリ不要な'html.parser'を指定
soup=BeautifulSoup(res.text,'html.parser')

#BeautifulSoupオブジェクトをprintにそのまま渡すと全文を表示する
#print(soup)

#タグで要素取得
ele=soup.find('title')#<title>コビトカバ</title>
#print(ele)

#要素のtextコンテントを表示
print(ele.text)#コビトカバ

#要素を結果セット(ResultSet)として取得
imgs=soup.find_all('img')
print(type(imgs))#<class 'bs4.element.resultSet'>
for img in imgs:
    #属性にアクセスするにはgetメソッドを使う
    print(img.get('src'))


#その他の要素の取得方法

#idを指定
div=soup.find(id='headerImageBox')
imgs=div.find_all('img')
print(type(div))#型がtagクラス型
#<class 'bs4.element.Tag'>

#classで取得
imgs=soup.select('.headerImage')#★★★最強説なので覚えるquerySelectorAllと一緒
#select戻り値複数形（配列）
for img in imgs:
    print(img.get('src'))



tds=soup.select('td:first-child') #tr td:first=child でもOK
for td in tds:
    print(td.text)

tds=soup.select(' td')
tds=tds[0: len(tds):3]
for td in tds:
    print(td.text)

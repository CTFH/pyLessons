#コピー元のファイルパスとコピー後のファイルパスを入力>>
#file1.txt, file1copy.tx
orgName,cpName=input('コピー元のファイルパスとコピー後のファイルパスをお入力>>').split(',')
with open(orgName,'r',encoding='utf-8')as reader, open(cpName, 'w',encoding='utf-8')as writer:
    for line in reader:
        writer.write(line)


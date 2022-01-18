text=input('今日は何をした？>>')
with open('diary.txt', 'a', encoding='utf-8') as file:
    file.write(text + '\n')

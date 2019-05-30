'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
'''

import requests
from IPython.display import clear_output

url = '699991.txt'
cnt = 0
files = []
r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + url)
text = r.text.split()
print(text[0])
while text[0] != 'We':
    r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + url)
    text = r.text.split()
    url = text[0]
    files.append(url)
    cnt += 1
    clear_output(wait=True)
    print(url)
print(url)
print(files)
print(*text)

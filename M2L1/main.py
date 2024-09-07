# Так можно прочитать весь файл
f = open('text.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()

# А так перезапишем файл полностью
f = open('text.txt', 'w', encoding='utf-8')
text = 'Новый текст'
f.write(text)
f.close()

# А вот сокращенная версия
with open('text.txt', 'r', encoding='utf-8') as f:
    print(f.read())
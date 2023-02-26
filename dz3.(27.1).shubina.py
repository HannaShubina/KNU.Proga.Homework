#27.02(a), Шубіна

import cgi

# Встановлюємо заголовок відповіді на HTML-документ
print("Content-type: text/html")
print()

# Отримуємо дані форми з введеними рядками
form = cgi.FieldStorage()
string1 = form.getvalue("string1", "")
string2 = form.getvalue("string2", "")

# Розбиваємо рядки на слова та зберігаємо їх у відповідні множини
words1 = set(string1.split())
words2 = set(string2.split())

# Знаходимо різницю множин та виводимо її на екран
common_words = words1 & words2
if len(common_words) == 0:
    print("<p>У введених рядках немає спільних слів.</p>")
else:
    print("<p>Спільні слова: " + ", ".join(sorted(common_words)) + ".</p>")

# Форма для введення рядків
print('<form method="post" action="script.py">')
print('<p>Рядок 1: <input type="text" name="string1" value="' + string1 + '"></p>')
print('<p>Рядок 2: <input type="text" name="string2" value="' + string2 + '"></p>')
print('<input type="submit" value="Знайти спільні слова">')
print('</form>')

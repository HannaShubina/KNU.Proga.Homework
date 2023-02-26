#Шубіна Ганна, 26.11


import urllib.request
import re
from datetime import datetime, timedelta

# Функція, яка повертає URL для запиту погоди для заданого міста
#також я додала "/ext", яке переходить саме на прогноз за 14 днів
def get_weather_url(city):
    return f"https://www.timeanddate.com/weather/ukraine/{city}/ext"

# Функція, яка отримує HTML-сторінку за заданим URL
def get_html(url):
    with urllib.request.urlopen(url) as response:
        return response.read()

# Функція, яка отримує дані погоди з HTML-сторінки
def get_weather_data(html):
    # Знаходимо поточну дату
    today = datetime.now().strftime('%A, %B %d, %Y')

    # Знаходимо прогноз температури на наступні 14 днів
    temperature_pattern = r"-?\d+\s*/\s*-?\d+\s*°?C?"
    temperatures = re.findall(temperature_pattern, html)

    return today, temperatures

# Запитуємо користувача назву міста
city = input("Введіть назву міста (англійською): ")

# Отримуємо HTML-сторінку з погодою
url = get_weather_url(city)
html = get_html(url)

# Отримуємо дані погоди з HTML-сторінки
today, temperatures = get_weather_data(html.decode())
print(temperatures)

# Виводимо результат
print(f"Поточна дата: {today}")
print("Прогноз температури на наступні 14 днів (максимальна / мінімальна):")
for i in range(14):
    day = (datetime.now() + timedelta(days=i)).strftime('%A, %B %d')
    print(f"{day}: {temperatures[i].split()[0]} / {temperatures[i].split()[2]}")

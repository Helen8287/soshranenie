import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "https://divan.ru/category/svet"
driver.get(url)
time.sleep(3)

lums = driver.find_elements(By.CSS_SELECTOR, 'div.WdR1o')

parsed_data = []

for lum in lums:
    try:
        name = lum.find_element(By.CSS_SELECTOR,'div.lsooF span').text
        price = lum.find_element(By.CSS_SELECTOR,'div.pY3d2 span').text
        url_elem = lum.find_element(By.CSS_SELECTOR,'a.ui-GPFV8.qUioe')
        url_value =  url_elem.get_attribute('href')
        parsed_data.append([name, price, url])

    except Exception as e:
        print(f"Произошла ошибка:{e}")

driver.quit()

with open("lum.csv", 'w', newline='', encoding='utf-8') as file:       # Прописываем открытие нового файла, задаём ему название и форматирование
                                                                       # 'w' означает режим доступа, мы разрешаем вносить данные в таблицу

    writer = csv.writer(file)  # Создаём объект, Используем модуль csv и настраиваем запись данных в виде таблицы

    writer.writerow(['Название', 'цена', 'ссылка'])   # Создаём первый ряд

    writer.writerows(parsed_data)       # Прописываем использование списка как источника для рядов таблицы

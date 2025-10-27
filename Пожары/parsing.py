import requests  
from bs4 import BeautifulSoup  
import pandas as pd  
'''Для первого сайта аналогично'''
for page_number in range(1, 4):
    # 1. Загружаем страницу по адресу url 
    url = f'https://yupest2.pythonanywhere.com/infrastructure_objects/?page={page_number}'
    response = requests.get(url)  
    soup = BeautifulSoup(response.text, 'html.parser')  

    # 2. Находим таблицу  
    table = soup.find('table')

    # 3. Извлекаем названия полей 
    columns = [col.text.strip() for col in table.find_all('th')]

    # 4. Извлекаем строки  
    data = []
    for row in table.find_all('tr')[1:]:  # Пропускаем заголовок  
        cols = row.find_all('td')  
        data.append([col.text.strip() for col in cols]) 

    # 5. Сохраняем в DataFrame и в файл CSV  
    df = pd.DataFrame(data, columns=columns) 
    if page_number == 1:
        df.to_csv('data_2.csv', mode='a', index=False, encoding='UTF-8')
    else:
        df.to_csv('data_2.csv', mode='a', header=False, index=False, encoding='UTF-8')
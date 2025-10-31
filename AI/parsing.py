import requests  
from bs4 import BeautifulSoup  
import pandas as pd  

# 1. Загружаем страницу по адресу url 
url = f'https://yupest2.pythonanywhere.com/riviya/'
response = requests.get(url)
response.raise_for_status() # Проверяет, не было ли ошибки при запросе
soup = BeautifulSoup(response.text, 'html.parser')

# 2. Находим заголовки h1  
data_location = soup.find_all('h1', {'name':'location'})
data_lattitude = soup.find_all('span', {'name': 'lattitude'})
data_longitude = soup.find_all('span', {'name': 'longitude'})
data_likes = soup.find_all('span', {'name': 'likes'})

headers = ['location', 'lattitude', 'longitude', 'likes']

data_for_csv = []

for i in range(len(data_location)):
    data_for_csv.append([data_location[i].text, data_lattitude[i].text, data_longitude[i].text, data_likes[i].text[:-2]])

df = pd.DataFrame(data_for_csv, columns=headers)
df.to_csv('data_new.csv', index=False, mode='a', encoding='UTF-8')

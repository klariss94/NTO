import requests  
from bs4 import BeautifulSoup  
import pandas as pd  

# 1. Загружаем страницу по адресу url 
url = f'https://yupest2.pythonanywhere.com/riviya/'
response = requests.get(url)  
soup = BeautifulSoup(response.text, 'html.parser')  

# 2. Находим заголовки h1  
data = soup.find_all('h1', {'name':'location'})
data_new = []

for element in data:
    data_new.append(str(element)[20:-5])

data_lat = soup.find_all('span', {'name':'lattitude'})

data_lon = soup.find_all('span', {'name':'longitude'})

coordinations = []

for i in range(len(data_lon)):
    coordinations.append(str(data_lat[i])[23:-7]+','+ str(data_lon[i])[23:-7])


df = pd.DataFrame(coordinations, data_new) 
df.to_csv('data_new.csv', mode='a', encoding='UTF-8')
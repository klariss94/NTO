import pandas as pd

# Загрузка данных из файлов CSV
fires_df = pd.read_csv('data_1.csv')  # файл с данными о природных пожарах
infrastructure_df = pd.read_csv('data_2.csv')  # файл с данными об инфраструктуре

# Объединение данных по ключам: LON_LAT и frname
merged_df = pd.merge(fires_df, infrastructure_df, on=['LON_LAT', 'frname'], how='inner')  # или how='outer', в зависимости от задачи

# Проверка результата
print(merged_df.head())

# Сохранение в CSV
merged_df.to_csv('merged_data.csv', index=False)

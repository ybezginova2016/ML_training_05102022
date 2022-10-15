import pandas as pd

# создаем простой набор данных с характеристиками пользователей
data = {
    'Name': ['Vladimir', 'Anna', 'Peter', 'Yulia'],
    'Location': ['Belgrade', 'Petersburg', 'London', 'Belgrade'],
    'Age': [36, 23, 19, 32]
}

data_pandas = pd.DataFrame(data)
print(data_pandas)

print()
print(data_pandas[data_pandas.Age > 30].reset_index().drop(columns='index'))
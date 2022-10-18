# Рассмотрим пример. Интернет-магазины с одинаковым ассортиментом
# «ЧехлоФон» и «АйДаЧехол» планируют слияние. В таблицах заданы
# фрагменты списков их складских запасов. В двух колонках указаны
# названия товаров и количество.

# Такая продукция есть на складе первого магазина — «ЧехлоФона»:
import numpy as np
import pandas as pd

quantity = [25, 63, 80, 91, 81, 55, 14, 76, 33, 71]
models = ['Чехол силиконовый для iPhone 8',
          'Чехол кожаный для iPhone 8',
          'Чехол силиконовый для iPhone XS',
          'Чехол кожаный для iPhone XS',
          'Чехол силиконовый для iPhone XS Max',
          'Чехол кожаный для iPhone XS Max',
          'Чехол силиконовый для iPhone 11',
          'Чехол кожаный для iPhone 11',
          'Чехол силиконовый для iPhone 11 Pro',
          'Чехол кожаный для iPhone 11 Pro',
         ]
stocks = pd.DataFrame(
    {
        'Quantity' : quantity,
        'Model Name': models
    }
)
print(stocks)


###### 1.Выберите из каждой таблицы столбец с количеством
# и преобразуйте в вектор.

quantity_1 = [25, 63, 80, 91, 81, 55, 14, 76, 33, 71]
models = ['Чехол силиконовый для iPhone 8',
          'Чехол кожаный для iPhone 8',
          'Чехол силиконовый для iPhone XS',
          'Чехол кожаный для iPhone XS',
          'Чехол силиконовый для iPhone XS Max',
          'Чехол кожаный для iPhone XS Max',
          'Чехол силиконовый для iPhone 11',
          'Чехол кожаный для iPhone 11',
          'Чехол силиконовый для iPhone 11 Pro',
          'Чехол кожаный для iPhone 11 Pro',
         ]
stocks_1 = pd.DataFrame({'Количество' : quantity_1}, index=models)

quantity_2 = [82, 24, 92, 48, 32, 45, 4, 34, 12, 1]
stocks_2 = pd.DataFrame({'Количество' : quantity_2}, index=models)

vector_of_quantity_1 =  stocks_1['Количество'].values
vector_of_quantity_2 =  stocks_2['Количество'].values
print("Запасы первого магазина:", vector_of_quantity_1,
      "\nЗапасы второго магазина:",vector_of_quantity_2)

# 2. Вычислите вектор со складским запасом объединённого
# интернет-магазина «АйДаЧехлоФон».

vector_of_quantity_united = vector_of_quantity_1 + vector_of_quantity_2
print(vector_of_quantity_united)

# 3. Постройте таблицу с ассортиментом объединённого магазина
stocks_united = pd.DataFrame(
    {
        'Quantity 1': quantity_1,
        'Quantity 2': quantity_2,
        'Quantity Total': vector_of_quantity_united
    }, index=models
)

print(stocks_united)
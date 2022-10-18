import numpy as np
import pandas as pd

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
stocks_united['Цена'] = [3000, 2100, 3200, 2200, 1800, 1700, 3800, 1200, 2300, 2900]
price_united = stocks_united['Цена'].values
print(price_united)

# 2. «АйДаЧехлоФон» объявил о 10%-й скидке на весь объединённый
# ассортимент. С учётом этой акции вычислите вектор с ценами.
# Напечатайте результат на экране (уже в прекоде).

price_discount_10 = 0.9 * price_united
stocks_united['Цена со скидкой 10%'] = price_discount_10.astype(int)
print(stocks_united)

# 3. После месяца скидок «АйДаЧехлоФон» поднял цены на 10%.
# Создайте прайс-лист с учётом повышения. Напечатайте результат
# на экране (уже в прекоде).
price_no_discount =  1.1 * price_discount_10
stocks_united['Повышенная на 10% цена'] = price_no_discount.astype(int)
print(stocks_united)

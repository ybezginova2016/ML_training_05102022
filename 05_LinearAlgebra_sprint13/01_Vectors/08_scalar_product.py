# Скалярное произведение векторов a и b обычно обозначается круглыми
# скобками (𝑎, 𝑏) или точкой 𝑎⋅𝑏.
# Вычислим это же скалярное произведение функцией numpy.dot()
# (от англ. «точка») и убедимся, что результаты совпадают

import numpy as np

volume = np.array([0.1, 0.3, 0.1])
content = np.array([0.4, 0.0, 0.1])

print(np.dot(volume, content))

# Ещё проще скалярное произведение вычисляется оператором
# матричного умножения (англ. Matrix multiplication).
# Он обозначается символом коммерческое эт (англ. commercial at),
# или «собака» (@):
import numpy as np

volume = np.array([0.1, 0.3, 0.1])
content = np.array([0.4, 0.0, 0.1])

print(volume @ content)

# Другая операция — поэлементное умножение оператором.
# Его результатом, в отличие от скалярного произведения,
# будет вектор:

import numpy as np

volume = np.array([0.1, 0.3, 0.1])
content = np.array([0.4, 0.0, 0.1])

print(volume * content)

# Рассмотрим пример. Вектор 𝑞 содержит количество каждого товара
# на складе наушников, а вектор 𝑐 — цены на эту продукцию.
# Общая стоимость всех товаров — это сумма произведений
# количества каждого товара на его цену, то есть скалярное
# произведение (𝑞, 𝑐).
# Таблица содержит количество наушников и цены на них в двух магазинах
# сети «Я вас услышал».
import pandas as pd

shop1_price = [20990, 11990, 5390, 3190, 1990, 10990, 5999, 2290, 8111, 3290]
shop1_quantity = [19, 11, 8, 15, 23, 7, 14, 9, 10, 4]

shop2_price = [20990, 12490, 4290, 2790, 2390, 10990, 4990, 2490, 8990, 3290]
shop2_quantity = [10, 16, 20, 9, 18, 12, 10, 11, 18, 22]

models = ['Apple AirPods Pro',
          'Apple AirPods MV7N2RU/A',
          'JBL Tune 120TWS',
          'JBL TUNE 500BT',
          'JBL JR300BT',
          'Huawei Freebuds 3',
          'Philips TWS SHB2505',
          'Sony WH-CH500',
          'Sony WF-SP700N',
          'Sony WI-XB400',
         ]
stocks1 = pd.DataFrame({'Цена':shop1_price,
                        'Количество':shop1_quantity}, index=models)
stocks2 = pd.DataFrame({'Цена':shop2_price,
                        'Количество':shop2_quantity}, index=models)

print('Магазин 1\n', stocks1, '\n')
print('Магазин 2\n', stocks2)

##### TASK ######
# Найдите стоимость всех товаров в первом и втором магазинах сети
# «Я вас услышал». Сохраните их в переменных stocks1_cost
# (англ. «стоимость запасов на складе») и stocks2_cost.
# Найдите суммарную стоимость товаров двух магазинов сети
# и сохраните её в переменной total_cost (англ. «общая стоимость»).

import numpy as np
import pandas as pd

shop1_price = [20990, 11990 , 5390, 3190, 1990, 10990, 5999, 2290, 8111 , 3290]
shop1_quantity = [19, 11, 8, 15, 23, 7, 14, 9, 10, 4]

shop2_price = [20990, 12490, 4290, 2790, 2390, 10990, 4990, 2490, 8990, 3290]
shop2_quantity = [10, 16, 20, 9, 18, 12, 10, 11, 18, 22]

models = ['Apple AirPods Pro',
          'Apple AirPods MV7N2RU/A',
          'JBL Tune 120TWS',
          'JBL TUNE 500BT',
          'JBL JR300BT',
          'Huawei Freebuds 3',
          'Philips TWS SHB2505',
          'Sony WH-CH500',
          'Sony WF-SP700N',
          'Sony WI-XB400',
         ]
stocks1 = pd.DataFrame({'Цена':shop1_price,
                        'Количество':shop1_quantity}, index=models)
stocks2 = pd.DataFrame({'Цена':shop2_price,
                        'Количество':shop2_quantity}, index=models)

stocks1_price = stocks1['Цена'].values
stocks1_quantity = stocks1['Количество'].values

stocks2_price = stocks1['Цена']
stocks2_quantity = stocks2['Количество'].values

# общая стоимость товаров в магазине 1
stocks1_cost = stocks1_price @ stocks1_quantity

# общая стоимость товаров в магазине 2
stocks2_cost = stocks2_price @ stocks2_quantity

total_cost = stocks1_cost + stocks2_cost

print('Общая стоимость всех товаров в сети:', total_cost, 'руб.')


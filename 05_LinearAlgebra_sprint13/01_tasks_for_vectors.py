# 1. Создайте два вектора: первый содержит все ответы на вопрос о цене,
# второй — о качестве. Выделите из таблицы столбец с данными, не преобразовывая его в список.

import numpy as np
import pandas as pd

reviews_values = [
    [68, 13], [80, 14], [92, 37],
    [34, 62], [87, 17], [29, 88],
    [56, 32], [34, 67], [62, 86],
    [23, 45], [73, 71], [50, 50]
]

df_reviews = pd.DataFrame(reviews_values, columns=['Price', 'Quality'])

# not creating a list of price and quality values
price = df_reviews['Price'].values
quality = df_reviews['Quality'].values

print('Price: {}'.format(price))
print('Quality: {}'.format(quality))

# columns are arrays!

###### TASK 2 ######
# Определите общее количество покупателей «НосиВипчик».
# Найдите вектор с оценками клиента с индексом
# 4 (нумерация индексов начинается с нуля).

# Функцией len() найдите длину столбца таблицы reviews['Price'].values.
# Функцией loc() извлеките четвёртую строку таблицы reviews.loc[4],
# а потом преобразуйте её в вектор.

visitors_count = len(price)
visitor4 = np.array(df_reviews.loc[4])
print("Number of customers:", visitors_count)
print("Customer 4:", visitor4)

###### TASK 3 ######
# 3. У таблицы есть атрибут values — это двумерный массив.
# Вызовом функции list() преобразуйте его в список векторов
# с оценками всех клиентов.

vector_list = list(df_reviews.values)
print(vector_list)



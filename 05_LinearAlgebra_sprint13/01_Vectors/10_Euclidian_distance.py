# Если векторы a=(𝑥_1, 𝑦_1)a=(x2, y2) и b=(𝑥_2, 𝑦_2)b=(x
# построены из одной точки, можно рассчитать евклидово расстояние
# (англ. Euclidian distance) между ними. Оно равно длине вектора
# b-ab−a, то есть модулю разности векторов.

import numpy as np

a = np.array([5, 6])
b = np.array([1, 3])
d = np.dot(a-b, a-b)**0.5
print('Расстояние между векторами a и b равно', d)

# Формулу евклидова расстояния между двумя векторами можно
# использовать для вычисления расстояния между точками. Для этого
# нужно провести векторы из нуля в эти точки и вычислить расстояние
# между векторами.


# Для расчёта расстояний в SciPy есть библиотека distance
# (англ. «расстояние»). А евклидово расстояние можно вычислить
# с помощью функции distance.euclidean():

import numpy as np
from scipy.spatial import distance

a = np.array([5, 6])
b = np.array([1, 3])
d = distance.euclidean(a, b)
print('Расстояние между точками a и b равно', d)

# Рассмотрим пример. Компания «Дрон Горыныч» из деревни Тетерье
# доставляет товары дронами. Примем Тетерье за начало отсчёта.
# Координаты остальных населенных пунктов отложим по осям XX и YY
# в километрах.

# Чтобы спланировать маршрут дрона, сохраним данные о доставке
# в три переменные:
# x_axis — координаты каждого населённого пункта по оси XX;
# y_axis — координаты по оси YY;
# shipments — среднее еженедельное количество доставок в каждый город.
# Эти данные объединим в датафрейме и выведем на экран:

import numpy as np
import pandas as pd

# координаты по оси X
x_axis = np.array([0., 0.18078584, 9.32526599, 17.09628721,
                      4.69820241, 11.57529305, 11.31769349, 14.63378951])

# координаты по оси Y
y_axis  = np.array([0.0, 7.03050245, 9.06193657, 0.1718145,
                      5.1383203, 0.11069032, 3.27703365, 5.36870287])

# англ. доставки
shipments = np.array([5, 7, 4, 3, 5, 2, 1, 1])

# англ. населённый пункт
village = ['Тетерье',
           'Журавец',
           'Корсунь',
           'Берёзовка',
           'Протасово',
           'Трудки',
           'Нижний Туровец',
           'Вышний Туровец']

data = pd.DataFrame({'x_coordinates_km': x_axis,
                     'y_coordinates_km': y_axis,
                     'deliveries': shipments}, index=village)

print(data)

# Расстояния между пунктами рассчитаем через длины векторов.
# Для этого извлечём координаты точек в переменную vectors.
vectors = data[['x_coordinates_km', 'y_coordinates_km']].values
print(vectors)

###### TASK 1 #######
# 1. Постройте таблицу расстояний между населёнными пунктами и
# сохраните её в переменной distances. Представьте данные как
# список списков. Каждая строка — это расстояние от одного населённого
# пункта до остальных.

# Добавьте в таблицу distances названия всех сёл и деревень.
# Обратите внимание, что здесь колонки называются не по правилам
# Python — кириллицей и с заглавной буквы. Названия деревень
# на латинице выглядят нечитабельно, а код должен понимать не
# только автор, но и другие разработчики.

import numpy as np
import pandas as pd
from scipy.spatial import distance

x_axis = np.array([0.0, 0.18078584, 9.32526599, 17.09628721,
                   4.69820241, 11.57529305, 11.31769349, 14.63378951])

y_axis = np.array([0.0, 7.03050245, 9.06193657, 0.1718145,
                   5.1383203, 0.11069032, 3.27703365, 5.36870287])

shipments = np.array([5, 7, 4, 3, 5, 2, 1, 1])

village = ['Тетерье',
           'Журавец',
           'Корсунь',
           'Берёзовка',
           'Протасово',
           'Трудки',
           'Нижний Туровец',
           'Вышний Туровец']

data = pd.DataFrame({'x_coordinates_km': x_axis,
                     'y_coordinates_km': y_axis,
                     'deliveries': shipments}, index=village)

vectors = data[['x_coordinates_km', 'y_coordinates_km']].values
print(vectors)

distances = []
for village_from in range(len(village)):
    row = []
    for village_to in range(len(village)):
        value = distance.euclidean(vectors[village_to], vectors[village_from])
        row.append(value)
    distances.append(row)

distances_df = pd.DataFrame(distances, index=village, columns=village)
print(distances_df)

# 2. Вы знаете, сколько заказов за неделю доставляют в каждую точку.
# Выберите оптимальный для склада компании «Дрон Горыныч» населённый
# пункт. Для этого найдите расстояние между пунктами, удвойте его
# (полёты туда и обратно) и умножьте на еженедельное количество
# доставок. Сохраните результат в списке shipping_in_week.
# Выберите населенный пункт с наименьшей суммарной дистанцией до
# соседей. Выведите результат на экран.

# Если склад в населённом пункте с индексом i, то расстояние между
# сёлами можно посчитать скалярным произведением:
# 2 * np.dot(np.array(distances[i]), shipments).
# Чтобы вычислить индекс минимального значения,
# вызовите метод idxmin() (англ. «индекс минимума»).
# Найдите его в документации.

shipping_in_week = []
for i in range(len(village)):
    dist = 2 * np.dot(np.array(distances[i]), shipments)
    shipping_in_week.append(dist)

shipping_in_week_df = pd.DataFrame({'distance': shipping_in_week}, index=village)

print(shipping_in_week_df)

print()
print()
# обратимся к серии и выберем первый столбец
print('Населённый пункт для склада:', shipping_in_week_df.idxmin().values[0])
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.idxmin.html
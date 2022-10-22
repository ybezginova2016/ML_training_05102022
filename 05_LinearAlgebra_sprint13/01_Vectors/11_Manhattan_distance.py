# Манхэттенское расстояние (англ. Manhattan distance), или расстояние
# городских кварталов,— сумма модулей разностей координат. Эту метрику
# предложил немецкий математик Герман Минковский. А название пошло
# от уличной планировки Манхэттена, где не применимо евклидово
# расстояние (его считают по прямой).

# 1. Напишите функцию для вычисления манхэттенского расстояния —
# manhattan_distance(). На вход она принимает два вектора, а
# возвращает расстояние. Решите задачу, создав векторизованную
# функцию. К циклам обращаться нельзя

# Получить вектор абсолютных значений по всем координатам можно
# так: np.abs(first - second).
import numpy as np

def manhattan_distance(first, second):
    dist_vect = sum(abs(first- second) for first, second in zip(first, second))
    return dist_vect

first = np.array([3, 11])
second = np.array([1, 6])

print(manhattan_distance(first, second))

# 2. Из трёх свободных такси найдите ближайшее в нужном районе
# Манхэттена.

# Заданы такие переменные:

# avenues_df, в которой сохранён список авеню и их координат;
# streets_df — список улиц и координат;
# address — перекрёсток, на котором клиент вызывает такси;
# taxies — места парковки такси.

# Найдите список расстояний всех машин до нужного адреса и
# сохраните результат в переменной taxies_distances.
# Определите порядковый номер ближайшего такси.

# Функция для вычисления манхэттенского расстояния называется
# distance.cityblock() (англ. «городские кварталы»).

# Чтобы найти минимальный индекс в массиве NumPy,
# вызовите функцию argmin() (от англ. «аргумент,
# соответствующий минимуму»).

import numpy as np
import pandas as pd
from scipy.spatial import distance

avenues_df = pd.DataFrame([0, 153, 307, 524], index=['Park', 'Lexington', '3rd', '2nd'])
streets_df = pd.DataFrame([0, 81, 159, 240, 324], index=['76', '75', '74', '73', '72'])
# print(avenues_df)
# print(streets_df)

address = ['Lexington', '74']
taxies = [
    ['Park', '72'],
    ['2nd', '75'],
    ['3rd', '76'],
]

address_vector = np.array([avenues_df.loc[address[0]], streets_df.loc[address[1]]])

taxi_distances = []

for arg in range(len(taxies)):
    taxi_vector = np.array(avenues_df.loc[taxies[arg]], streets_df.loc[taxies[arg]])
    taxi_distances.append(distance.cityblock(taxi_vector, address_vector))

index = np.argmin(taxi_distances)
print(taxies[index])
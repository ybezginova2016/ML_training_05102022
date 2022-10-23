
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

address = ['Lexington', '74']
taxies = [
    ['Park', '72'],
    ['2nd', '75'],
    ['3rd', '76'],
]

# address_vector = np.array([avenues_df.loc[address[0]], streets_df.loc[address[1]]])
# taxi_distances = []
#
# for arg in range(len(taxies)):
#     # taxi_vector = np.array([avenues_df.loc[taxies[arg]], streets_df.loc[taxies[arg]]])
#     # taxies[arg] - это список из двух значений. Чтобы извлечь нужный вектор из avenue_df, нужно сделать так:
#     taxi_vector = np.array([avenues_df.loc[taxies[arg][0]], streets_df.loc[taxies[arg][1]]])
#     taxi_distances.append(distance.cityblock(taxi_vector, address_vector))
#
# index = np.argmin(taxi_distances)
# print(taxies[index])

address_vector = np.array([avenues_df.loc[address[0]].values[0], streets_df.loc[address[1]].values[0]])
taxi_distances = []

for arg in range(len(taxies)):
    # taxi_vector = np.array([avenues_df.loc[taxies[arg]], streets_df.loc[taxies[arg]]])
    # taxies[arg] - это список из двух значений. Чтобы извлечь нужный вектор из avenue_df, нужно сделать так:
    taxi_vector = np.array([avenues_df.loc[taxies[arg][0]].values[0], streets_df.loc[taxies[arg][1]].values[0]])
    taxi_distances.append(distance.cityblock(taxi_vector, address_vector))

index = np.argmin(taxi_distances)
print(taxies[index])
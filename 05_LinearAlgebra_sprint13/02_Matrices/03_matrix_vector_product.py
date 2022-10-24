# Умножение матрицы на вектор
# Что получится, если умножить матрицу на вектор? Вектор!
import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]])

b = np.array([7, 8, 9])

print(np.dot(A, b))
print(A.dot(b))

# Чтобы умножение было корректным, размер вектора должен быть равен
# ширине матрицы.

# Рассмотрим пример. Мобильный оператор «Шмеляйн» предлагает
# пакеты услуг: «За рулём» и «В метро». Каждый действует месяц и
# состоит из минут разговора, количества СМС и мегабайтов
# интернет-трафика. В среднем пользователи набирают по 4-5 пакетов
# в месяц:

import numpy as np
import pandas as pd

services = ['Минуты', 'СМС', 'Мбайты']

packs_names = ['«За рулём»', '«В метро»']

packs = np.array([
    [20, 5],
    [2, 5],
    [500, 1000]])

print('Составы пакетов')
print(pd.DataFrame(packs, columns=packs_names, index=services))
print()

clients_packs = np.array([
    [1, 2],
    [2, 3],
    [4, 1],
    [2, 3],
    [5, 0]])

print('Пакеты клиентов')
print(pd.DataFrame(clients_packs, columns=packs_names))
print()

# Рассчитайте количество минут разговора, СМС и объём
# интернет-трафика, которые потратил за месяц клиент №1.
# Сохраните результат в переменной client_services и
# напечатайте результат на экране
import numpy as np
import pandas as pd

services = ['Минуты', 'СМС', 'Мбайты']
packs_names = ['«За рулём»', '«В метро»']

packs = np.array([
    [20, 5],
    [2, 5],
    [500, 1000]])

clients_packs = np.array([
    [1, 2],
    [2, 3],
    [4, 1],
    [2, 3],
    [5, 0]])

client = 1
print('Пакеты клиента')
print(pd.DataFrame(clients_packs[client], index=packs_names, columns=['']))
print()

# Извлекаем вектор с данными клиента № 1

client_vector = clients_packs[1, :]
# two way to mupltiply vector client_vector to a matrix packs
# 1
# client_services = packs.dot(client_vector)

# 2
client_services = np.dot(packs, client_vector)
print("Минуты, СМС, Мбайты")
print(client_services)

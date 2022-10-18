import numpy as np

vector1 = np.array([2, 3])
vector2 = np.array([6, 2])
vector_mean = .5*(vector1+vector2)
print(vector_mean)
# Среднее значение мы назвали vector_mean (англ. mean, «средний»).
# Первая координата нового вектора — это среднее значение первых
# координат векторов vector1 и vector2, а вторая — среднее вторых
# координат.
# Изобразим на плоскости эти векторы. Строим вектор vector1+vector2,
# затем умножаем его на 0.50.5.
import numpy as np
import matplotlib.pyplot as plt

vector1 = np.array([2, 3])
vector2 = np.array([6, 2])
vector_mean = .5*(vector1+vector2)

plt.figure(figsize=(7, 6))
plt.axis([0, 8.4, -1, 6])
arrow1 = plt.arrow(0, 0, vector1[0], vector1[1],
                   head_width=0.3, length_includes_head="True", color='b')
arrow2 = plt.arrow(0, 0, vector2[0], vector2[1],
                   head_width=0.3, length_includes_head="True", color='g')
arrow_sum = plt.arrow(0, 0, vector1[0]+vector2[0], vector1[1]+vector2[1],
                   head_width=0.3, length_includes_head="True", color='r')
arrow_mean = plt.arrow(0, 0, vector_mean[0], vector_mean[1],
                   head_width=0.3, length_includes_head="True", color='m')
plt.plot(vector1[0], vector1[1],'ro')
plt.plot(vector2[0], vector2[1], 'ro')
plt.plot(vector_mean[0], vector_mean[1], 'ro')
plt.legend([arrow1, arrow2, arrow_sum, arrow_mean], ['vector1', 'vector2', 'vector1+vector2', 'vector_mean'], loc='upper left')
plt.grid(True)
plt.show()

# Пример: посчитаем, какие оценки в среднем ставит типичный покупатель
# интернет-магазина одежды «НосиВипчик».
# Чтобы вычислить среднюю оценку удовлетворённости стоимостью,
# примените функцию sum. Она вычислит сумму всех элементов вектора.

import numpy as np
import pandas as pd

reviews_values = [
    [68,18], [81,19], [81,22], [15,75], [75,15], [17,72],
    [24,75], [21,91], [76, 6], [12,74], [18,83], [20,62],
    [21,82], [21,79], [84,15], [73,16], [88,25], [78,23],
    [32, 81], [77, 35]]
reviews = pd.DataFrame(reviews_values, columns=['Цена', 'Качество'])

price = reviews['Цена'].values  # массив NumPy со всеми оценками стоимости
sum_prices = sum(price)  # сумма всех оценок стоимости
average_price_rev = sum_prices/len(price)  # среднее значение оценки стоимости
print(average_price_rev)

# 1. Вычислите среднее значение оценки удовлетворённости качеством.
# А функция print(average_quality_rev) напечатает результат на экране.
quality = reviews['Качество']
sum_quality = sum(quality)
average_quality_rev = sum_quality / len(reviews['Качество'])
print(average_quality_rev)

# 2. Мы добавили в код расчёт средней цены и сохранили её в
# переменной average_price_rev. Теперь сохраните в массив average_rev:
# среднюю оценку цены, среднюю оценку качества.

average_rev = np.array([average_price_rev, average_quality_rev])
print(average_rev)

# 3. Обозначьте на координатной плоскости найденное среднее значение.
# Можно ли считать получившийся вектор оценками типичного покупателя?
# Напечатайте результат на экране.

plt.figure(figsize=(7, 7))
plt.axis([0, 100, 0, 100])
plt.plot(average_rev[0], average_rev[1], 'mo', markersize=15)
plt.plot(price, quality, 'ro')
plt.xlabel('Цена')
plt.ylabel('Качество')
plt.grid(True)
plt.title("Распределение оценок и среднее значение по всей выборке")
plt.show()


# 4. Вычислите средние оценки отдельно для клиентов, которые пришли
# с первого сайта-агрегатора (масс-маркет) и со второго (люкс).
# Результат должен появиться на экране.
import numpy as np
import pandas as pd

reviews_values = [
    [68,18], [81,19], [81,22], [15,75], [75,15], [17,72],
    [24,75], [21,91], [76, 6], [12,74], [18,83], [20,62],
    [21,82], [21,79], [84,15], [73,16], [88,25], [78,23],
    [32, 81], [77, 35]]
reviews = pd.DataFrame(reviews_values, columns=['Цена', 'Качество'])

clients_1 = []
clients_2 = []
for client in list(reviews.values):
    if client[0] < 40 and client[1] > 60:
        clients_2.append(client)
    else:
        clients_1.append(client)

average_client_1 = sum(clients_1) / len(clients_1)
print('Средняя оценка пришедших с первого агрегатора: ', average_client_1)

average_client_2 = sum(clients_2) / len(clients_2)
print('Средняя оценка пришедших со второго агрегатора: ', average_client_2)


# 5. Изобразите найденные значения средних на диаграмме с оценками
# отдельных клиентов. Можно ли считать каждое найденное среднее
# оценкой типичного клиента этой группы? Выведите результат на экран.
plt.figure(figsize=(7, 7))
plt.axis([0, 100, 0, 100])

# изображаем среднее для группы 1
# 'b' — синий цвет (англ. blue)
plt.plot(average_client_1[0], average_client_1[1],
         'bo', markersize=15)

# изображаем среднее для группы 2
# 'g' — зелёный цвет (англ. green)
plt.plot(average_client_2[0], average_client_2[1],
         'go', markersize=15)
plt.plot(price, quality, 'ro')
plt.xlabel('Цена')
plt.ylabel('Качество')
plt.grid(True)
plt.title("Распределение оценок и среднее значение для каждой группы")
plt.show()

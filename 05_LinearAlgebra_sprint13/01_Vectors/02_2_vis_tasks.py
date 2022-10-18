import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Изобразите стрелкой вектор [75, 15] из кейса об интернет-магазине
# одежды «НосиВипчик».

vector = np.array([75, 15])

plt.figure(figsize=(5, 5))
plt.axis([0, 100, 0, 50])
plt.arrow(0, 0, vector[0], vector[1],
    head_width=3,
    length_includes_head='True',
    color='r')

plt.xlabel('Price')
plt.ylabel('Quality')
plt.grid(True)
plt.show()

# 2. Представьте все двумерные векторы с оценками
# клиентов интернет-магазина «НосиВипчик» в виде
# точек на плоскости.
# Какие клиенты с какого агрегатора пришли?

# Передайте в функцию plt.plot() векторы с
# ценами и качеством.

reviews_values = [
    [68, 13], [80, 14], [92, 37],
    [34, 62], [87, 17], [29, 88],
    [56, 32], [34, 67], [62, 86],
    [23, 45], [73, 71], [50, 50]
]

reviews = pd.DataFrame(reviews_values, columns=['Price', 'Quality'])

price = reviews['Price'].values
quality = reviews['Quality'].values

plt.plot(price,
         quality,
         'ro')
plt.xlabel('Price')
plt.ylabel('Quality')
plt.grid(True)
plt.show()
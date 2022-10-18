# Векторизация метрик
# Запишем функции для измерения метрик качества через векторы.
# Как применить векторизацию к метрикам качества? Разберём на примере.
# В переменной target сохраним набор фактических значений,
# а в predictions — предсказанных. Оба набора типа np.array.

import numpy as np

target = np.array([0.9, 1.2, 1.4, 1.5, 1.9, 2.0])
predictions = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])

# Для вычисления метрик качества применим стандартные функции NumPy:
# sum() (чтобы найти сумму элементов массива);
# mean() (для расчёта их среднего значения).
# Вызовем их в формате: <имя массива>.sum() и <имя массива>.mean().
# Например, средний квадрат отклонения (MSE) вычисляется по формуле.

# Запишем эту формулу с применением sum():
def mse1(target, predictions):
    n = target.size
    return((target - predictions)**2).sum()/n
# Заметили, что сумма нескольких чисел, поделённая на их количество,
# — это среднее значение? Запишем формулу MSE проще — с применением
# функции mean():
def mse2(target, predictions):
    return((target - predictions)**2).mean()
# Чтобы убедиться, что результаты вычислений совпадают, применим
# к массивам target и predictions оба варианта функции MSE:

print(mse1(target, predictions), mse2(target, predictions))

##### TASK 1 #####
# 1. Напишите функцию для вычисления MAE с применением метода
# mean(). Посчитайте MAE и напечатайте результат на экране.

import numpy as np

def mae(target, predictions):
    mae = 1 / target.size * ((abs(target - predictions)).sum())
    return mae

target = np.array([0.9, 1.2, 1.4, 1.5, 1.9, 2.0])
predictions = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
print(mae(target, predictions))

# 2. Рассчитайте RMSE по этой формуле:
import numpy as np
import math

def rmse(target, predictions):
    mse = (1 / target.size * (target - predictions)**2).sum()
    return math.sqrt(mse)

target = np.array([0.9, 1.2, 1.4, 1.5, 1.9, 2.0])
predictions = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
print(rmse(target, predictions))



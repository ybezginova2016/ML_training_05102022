# https://www.askpython.com/python-modules/numpy/numpy-vectorization
import numpy as np

def foo(a, b):
    """
    If a > b return a + b,
    else return a - b.
    """
    if a >= b:
       return a + b
    else:
       return a - b

# Create a vectorized version of foo
vecfoo = np.vectorize(foo)
print(vecfoo(np.arange(5), 5))

a = np.array([1, 2, 3, 4])
b = 2

vecfoo =  np.vectorize(foo)
res = vecfoo(a, b)
print(type(res[0]))

# Векторизованные функции

# Научимся писать функции через векторы, векторизованные функции.
# Средства библиотеки NumPy позволяют производить и другие операции
# над векторами. Применив функцию np.array, после умножения и
# деления двух массивов одного размера получим новый вектор
# такого же размера:

import numpy as np

array1 = np.array([2, -4, 6, -8])
array2 = np.array([1, 2, 3, 4])
array_mult = array1 * array2
array_div = array1 / array2
print("Произведение двух массивов: ", array_mult)
print("Частное двух массивов: ", array_div)

# Если арифметические операции производятся над массивом и
# отдельным числом, то действие применяется к каждому элементу
# массива. И снова образуется массив такого же размера.
# Чтобы проверить, произведём над массивом и числом операции
# сложения, вычитания и деления:
import numpy as np

array2 = np.array([1, 2, 3, 4])
array2_plus_10 = array2 + 10
array2_minus_10 = array2 - 10
array2_div_10 = array2 / 10
print("Сумма: ", array2_plus_10)
print("Разность: ", array2_minus_10)
print("Частное массива и числа: ", array2_div_10)

# К массиву также поэлементно применимы и стандартные
# математические функции, например, возведение в степень
# или логарифмы.
# Возведём массив во вторую степень:
import numpy as np

numbers_from_0 =  np.array([0, 1, 2, 3, 4])
squares = numbers_from_0**2
print(squares)

# Всё это можно сделать и циклами над списками. Но операции с векторами
# в библиотеке NumPy работают быстрее.
# Рассмотрим пример. Среди элементов массива values максимальное
# и минимальное значения — это некоторые числа MAX и MIN при условии,
# что MAX>MIN. Для анализа данные нужно преобразовать.
# Каждый элемент 𝑥 нашего массива должен перейти в число в
# интервале от 0 (MIN) до 1 (MAX). Формула функции min_max_scale
# (англ. «масштабирование методом минимума-максимума»)

import numpy as np
def min_max_scale(values):
    return (values - min(values)) / (max(values) - min(values))

our_values = np.array([-20, 0, 0.5, 80, -1])
print(min_max_scale(our_values))

# Иногда значения могут быть сколь угодно большими.
# Их нужно преобразовать так, чтобы все значения попали в
# интервал от 0 до 1. Для этого применяют логистическую функцию,
# или логистическое преобразование:

# где exp() — это экспонента (от лат. exponere, «выставлять»).
# Она возводит e — число Эйлера (англ. Euler number) — в степень
# аргумента. Число названо в честь швейцарского математика
# Леонарда Эйлера, приблизительно равно 2.718281828.

##### TASK #####
# Напишите функцию logistic_transform(), выполняющую логистическое
# преобразование. Примените её ко всем элементам массива.
import numpy as np

def logistic_transform(values):
    return 1 / (1+ np.exp(-values))

our_values = np.array([-20, 0, 0.5, 80, -1])
print(logistic_transform(our_values))


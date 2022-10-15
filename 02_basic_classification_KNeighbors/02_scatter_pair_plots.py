import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from IPython.display import display
plt.rc('font', family='Verdana')
from sklearn.model_selection import train_test_split
# train_test_split - это функция, которая перемешивает набор данных
# и разбивает его на две части

from sklearn.datasets import load_iris
iris_dataset = load_iris()

# X - features
# y - labels

X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=1)

# Перед разбиением функция train_test_split перемешивает набор данных с помощью генератора
#  псевдослучайных чисел. Если мы просто возьмем 25% наболюдений в качество
#  тестового набора, все точки будут иметь метку 2, поскольку все точки
# данных отсортированы по меткам:
print('Targets: {} \n'.format(iris_dataset['target']))

# Смотрим, как произошло разбиение исходоного набора данных
print('X_train array shapr: {}'.format(X_train.shape))
print('y_train array shapr: {}'.format(y_train.shape))

print('X_test array shapr: {}'.format(X_test.shape))
print('X_test array shapr: {}'.format(X_test.shape))

# Перед тем, как обучать модель, визуализируем данные, чтобы увидеть проблемы данных
# scatterplot matrix or pair plots

# создаем dataFrame из данных в массиве X_train
# маркируем столбцы, используя строки в iris_dataset.feature_names
iris_dataFrame = pd.DataFrame(X_train, columns=iris_dataset.feature_names)

# creating scatterplot matrix from dataFrame
import mglearn
grr = pd.plotting.scatter_matrix(iris_dataFrame, c=y_train, figsize=(15, 13),
                           hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)
print(iris_dataFrame)
plt.show()

# From pair plot видим, что три цвета означают три разных класса. Значит,
# модель машинного обучения сможет научиться разделять их.



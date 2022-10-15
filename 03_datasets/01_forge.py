# import numpy as np
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# knn = KNeighborsClassifier(n_neighbors=1)
import matplotlib.pyplot as plt
import mglearn

# генерируем набор данных forge для двухклассовой классификации, который
# содержит два признака
X, y = mglearn.datasets.make_forge()
# print(X, y)
mglearn.discrete_scatter((X[:, 0]), X[:, 1], y)
plt.legend(["Class 0", "Class 1"], loc=5)
plt.xlabel("The first label")
plt.ylabel("The second label")
print("Shape of an array X: {}".format(X.shape))
plt.title('Диаграмма рассеяния для набора данных forge. \nНабор состоит из 26 точек и 2 признаков.')
plt.show()
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)

iris_dataset = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=1)

print(knn.fit(X_train, y_train))

X_new = np.array([[5, 2.9, 1, 0.2]])
prediction = knn.predict(X_new)
print("Forecast: {}".format(prediction))
print('Forecasted labels: {}'.format(iris_dataset['target_names'][prediction]))

#### Using test sample
y_pred = knn.predict(X_test)
print('Прогнозы для тестового набора: \n {}'.format(y_pred))

# Accuracy (правильность)
print('Accuracy: {:.2f}'.format(np.mean(y_pred == y_test)))
print('Accuracy: {:.2f}'.format(knn.score(X_test, y_test)))
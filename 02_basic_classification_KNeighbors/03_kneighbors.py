# k в методе ближайших соседей означает, что вместо того, чтобы использовать
# лишь ближайшего соседа новой точки данных, мы в ходе обучения можем рассмотреть
# любое фиксированное число соседей k = 3 or 5.

# В scikit-learn все модели машинного обучения реализованы в собственных классах,
# называемых классами Estimator. Алгоритм классификации на основе метода k
# ближайших соседей реализован в класификаторе KNeighborsClassifier модуля
# neighbors. Сначала нужно создать объект=-экземпляр класса.

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)

# Для обучения модели на обучающем наборе, мы вызываем метод fit объекта knn,
# который принимает в качестве аргументов массив NumPy X_train,
# содержащий обучающие данные, и массив y_train, соответствующий обучающим меткам:
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris_dataset = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=1)

print(knn.fit(X_train, y_train))
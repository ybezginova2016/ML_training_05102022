# 2. К классу NearestNeighborClassificator добавьте метод predict(). Возьмите за основу уже
# написанную функцию nearest_neighbor_predict() — метод должен вернуть предсказание в виде Series.
# Получите предсказания, есть кондиционеры или нет. Напечатайте результат на экране (уже в прекоде).

import numpy as np
import pandas as pd
from scipy.spatial import distance

columns = ['комнаты', 'площадь', 'кухня', 'пл. жилая', 'этаж', 'всего этажей', 'кондиционер']

df_train = pd.DataFrame([
    [1, 38.5, 6.9, 18.9, 3, 5, 1],
    [1, 38.0, 8.5, 19.2, 9, 17, 0],
    [1, 34.7, 10.3, 19.8, 1, 9, 0],
    [1, 45.9, 11.1, 17.5, 11, 23, 1],
    [1, 42.4, 10.0, 19.9, 6, 14, 0],
    [1, 46.0, 10.2, 20.5, 3, 12, 1],
    [2, 77.7, 13.2, 39.3, 3, 17, 1],
    [2, 69.8, 11.1, 31.4, 12, 23, 0],
    [2, 78.2, 19.4, 33.2, 4, 9, 0],
    [2, 55.5, 7.8, 29.6, 1, 25, 1],
    [2, 74.3, 16.0, 34.2, 14, 17, 1],
    [2, 78.3, 12.3, 42.6, 23, 23, 0],
    [2, 74.0, 18.1, 49.0, 8, 9, 0],
    [2, 91.4, 20.1, 60.4, 2, 10, 0],
    [3, 85.0, 17.8, 56.1, 14, 14, 1],
    [3, 79.8, 9.8, 44.8, 9, 10, 0],
    [3, 72.0, 10.2, 37.3, 7, 9, 1],
    [3, 95.3, 11.0, 51.5, 15, 23, 1],
    [3, 69.3, 8.5, 39.3, 4, 9, 0],
    [3, 89.8, 11.2, 58.2, 24, 25, 0],
], columns=columns)

train_features = df_train.drop('кондиционер', axis=1)
train_target = df_train['кондиционер']

df_test = pd.DataFrame([
    [1, 36.5, 5.9, 17.9, 2, 7, 0],
    [2, 71.7, 12.2, 34.3, 5, 21, 1],
    [3, 88.0, 18.1, 58.2, 17, 17, 1],
], columns=columns)

test_features = df_test.drop('кондиционер', axis=1)


def nearest_neighbor_predict(train_features, train_target, new_features):
    distances = []
    for i in range(train_features.shape[0]):
        vector = train_features.loc[i].values
        distances.append(distance.euclidean(new_features, vector))
    best_index = np.array(distances).argmin()
    return train_target.loc[best_index]


class NearestNeighborClassificator:
    def fit(self, features_train, target_train):
        self.features_train = features_train
        self.target_train = target_train

    def predict(self, new_features):
        answers = []
        for i in range(len(new_features)):
            vector = new_features.loc[i].values
            answers.append(nearest_neighbor_predict(self.features_train, self.target_train, vector))
        return pd.Series(answers)


model = NearestNeighborClassificator()
model.fit(train_features, train_target)
new_predictions = model.predict(test_features)
print(new_predictions)
import numpy as np
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
print("Keys of the dataset cancer(): \n {}".format(cancer.keys()))
print("Shape of the dataset cancer(): 569 features and 30 targets \n{}".format(cancer.data.shape))

#  Из 569 точек данных 212 помечены как злокачественные, а 357 как доброкачественные
print("Number of examples for each class - malignant and benign: \n {}".format(
    {n: v for n,
     v in zip(cancer.target_names,
              np.bincount(cancer.target))}
))

print("Feature names: \n {}".format(cancer.feature_names))
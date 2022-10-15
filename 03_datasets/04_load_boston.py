import mglearn.datasets
import numpy as np
from sklearn.datasets import load_boston

boston = load_boston()
print("Shape of data array boston(): \n {}".format(boston.data.shape))

X, y = mglearn.datasets.load_extended_boston()
print("Shape of an array X: {}".format(X.shape))
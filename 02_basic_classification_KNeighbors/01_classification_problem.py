from sklearn.datasets import load_iris
iris_dataset = load_iris()

print('Keys for iris_dataset: \n{}'.format(iris_dataset.keys()))
# DESCR - это краткое описание набора данных
print(iris_dataset['DESCR'][:193] + '\n...')

# target_names - an array for training the model
print('Targets names: {}'.format(iris_dataset['target_names']))
# feature_names - features
print('Features names: {}'.format(iris_dataset['feature_names']))

print('Type of an array: {}'.format(type(iris_dataset['data'])))
print('Shape of an array: {}'.format(iris_dataset['data'].shape))

# Shape of an array: (150, 4) - значит, в массиве содержится
# 150 различных цветков по 4 признакам

print("Target values: \n".format(iris_dataset['target']))
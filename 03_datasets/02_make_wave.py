import matplotlib.pyplot as plt
import mglearn

X, y = mglearn.datasets.make_wave(n_samples=40)
plt.plot(X, y, 'o')
plt.ylim(-3, 3)
plt.xlabel("Label")
plt.ylabel("Target")
plt.title('График для набора данных wave, \nпо оси х отложен признак, по оси y - целевая переменная')
plt.show()
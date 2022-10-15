# %matplotlib notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
# generating a set from -10 to 10 c 100 steps
x = np.linspace(-10, 10, 100)

y = np.sin(x)

plt.plot(x, y, marker="x")
plt.show()

# простой линейный график синусоидальной функции с использованием matplolib

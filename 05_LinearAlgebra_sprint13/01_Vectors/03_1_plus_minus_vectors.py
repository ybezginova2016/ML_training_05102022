# Сложение и вычитание векторов
# Векторы можно складывать и вычитать, если они одного размера.
# К вектору vector1 [2, 3] прибавим vector2 [6, 2]:
import numpy as np

vector1 = np.array([2, 3])
vector2 = np.array([7, 4])
vectors_sum = vector1 + vector2

print(vectors_sum)
# Из вектора vector2 вычтем vector1:
substraction = vector2 - vector1
print(substraction)
# Изобразим эти векторы стрелками на плоскости:
import matplotlib.pyplot as plt

plt.figure(figsize=(7, 7))
plt.axis([0, 10, -4, 10])
arrow1 = plt.arrow(0, 0, vector1[0], vector1[1], head_width=0.3,
                   length_includes_head="True", color='b')

arrow2 = plt.arrow(0, 0, vector2[0], vector2[1], head_width=0.3,
                   length_includes_head="True", color='g')
arrow3 = plt.arrow(0, 0, vectors_sum[0], vectors_sum[1], head_width=0.3,
                   length_includes_head="True", color='m')
arrow4 = plt.arrow(0, 0, substraction[0], substraction[1], head_width=0.3,
                   length_includes_head="True", color='r')
# Построим вектор разности subtraction:
arrow1new = plt.arrow(vector2[0], vector2[1], -vector1[0], -vector1[1],
                      head_width=0.3, length_includes_head='True',
                      color='b')
# Если от конца синего вектора vector1 отложить вектор, равный
# по длине и направлению зелёному vector2, то получится красный
# вектор sum_of_vectors
arrow2new = plt.arrow(vector1[0], vector1[1], vector2[0], vector2[1],
                      head_width=0.3, length_includes_head='True', color='r')
plt.plot(0, 0, 'ro')
plt.legend([arrow1, arrow2, arrow3, arrow4],
           ['vector1', 'vector2', 'vectors_sum', 'substraction'],
           loc='lower left')
plt.grid(True)
plt.show()
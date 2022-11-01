import numpy as np

# Задаём систему в матричном виде.
A = np.array([[0, 1], [8, 1]])
y = np.array([10, 7])

# Считаем обратную матрицу.
A_inv = np.linalg.inv(A)

# Находим решение системы.
result = A_inv @ y

print("k =", result[0])
print("m =", result[1])

##### Решим систему уравнений с тремя переменными
import numpy as np

# Задаём систему в матричном виде.
A = np.array([[1, 2, 1], [2, 1, 2], [3, 3, 1]])
y = np.array([8, 10, 12])

# Считаем обратную матрицу.
A_inv = np.linalg.inv(A)

# Находим решение системы.
result = A_inv @ y

print("a =", result[0])
print("b =", result[1])
print("c =", result[2])
print()
#### TASK 2 ####

# Найдите решение системы уравнений, заданной матрично.
# Используйте Python. Результат сохраните в переменной result.
# Полученный результат выведите на экран.
import numpy as np
A = np.array([[-36,  30,   7,   7],
       [  7, -38,   0,   5],
       [-10, -19,  33, -18],
       [ 48,  49,  26,  22]])
y = np.array([ -7, -44,   1,   7])

# Считаем обратную матрицу.
A_inv = np.linalg.inv(A)

# Находим решение системы.
result2 = A_inv @ y

print("a =", result2[0])
print("b =", result2[1])
print("c =", result2[2])
print("d =", result2[3])
print()
print(result2)
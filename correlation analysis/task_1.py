# 2
import numpy as np
from math import sqrt

n = 14
x = [2.8, 2.2, 3.0, 3.5, 3.2, 3.7, 4.0, 4.8, 6.0, 5.4, 5.2, 5.4, 6.0, 9.0]
y = [6.7, 6.9, 7.2, 7.3, 8.4, 8.8, 9.1, 9.8, 10.6, 10.7, 11.1, 11.8, 12.1, 12.4]
alpha = 0.05

r_ = np.corrcoef(x, y)
print("Выборочное значение коэффициента корреляции (с помощью numpy)\n", r_)

# by formulas
x_ = sum(x) / n
y_ = sum(y) / n
r_ = sum([(x[i] - x_) * (y[i] - y_) for i in range(n)]) / \
     sqrt(sum([(x[i] - x_) ** 2 for i in range(n)]) * sum([(y[i] - y_) ** 2 for i in range(n)]))
print("Выборочное значение коэффициента корреляции (по формулам)\n", r_)




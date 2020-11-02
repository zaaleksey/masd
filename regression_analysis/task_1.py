# Парная регрессия
import numpy as np

n = 50
x = [5 + i for i in range(0, 40, 5)]
print('x =', x)
y = [100 + i for i in range(0, 100, 20)]
print('y =', y)

freq = [
    [2, 1, 0, 0, 0, 0, 0, 0],
    [3, 4, 3, 0, 0, 0, 0, 0],
    [0, 0, 5, 10, 8, 0, 0, 0],
    [0, 0, 0, 1, 0, 6, 1, 1],
    [0, 0, 0, 0, 0, 0, 4, 1]
]

print()
X, Y = [], []
for i in range(len(y)):
    for j in range(len(x)):
        X += [x[j]] * freq[i][j]
for i in range(len(y)):
    Y += [y[i]] * sum(freq[i])

print('X =', X, len(X))
print('Y =', Y, len(Y))

print('\nY на X')
# первый способ (по формулам)
b1 = (np.sum((X - np.mean(X)) * (Y - np.mean(Y)))) / (np.sum((X - np.mean(X)) ** 2))
print('b1 =', b1)
b0 = np.mean(Y) - b1 * np.mean(X)
print('b0 =', b0)

print('\nX на Y')
# второй способ
b1 = np.corrcoef(Y, X)[0][1] * (np.std(X) / np.std(Y))
print('b1 =', b1)
b0 = np.mean(X) - b1 * np.mean(Y)
print('b0 =', b0)

# Множественная регрессия
import numpy as np

n = 10
q = 2
alpha = 0.05
x1 = np.array([8, 11, 12, 9, 8, 8, 9, 9, 8, 12])
x2 = np.array([5, 8, 8, 5, 7, 8, 6, 4, 5, 7])
x = np.array([[1] * n, x1, x2]).transpose()
y = np.array([[5], [10], [10], [7], [5], [6], [6], [5], [6], [8]])
# print('x =\n', x)
# print('y =\n', y)

# нахождение аналитического уравнения
XT_X = x.transpose().dot(x)
print('XT_X =\n', XT_X)

XT_Y = x.transpose().dot(y)
print('XT_Y =\n', XT_Y)

Theta = np.linalg.inv(XT_X).dot(XT_Y)
print('Theta =\n', Theta)

# множественный коэффициент корреляции
ThetaT = Theta.transpose()
ThetaT_XT_Y = ThetaT.dot(XT_Y)
print('ThetaT_XT_Y =', ThetaT_XT_Y)
YT_Y = y.transpose().dot(y)
print('YT_Y =', YT_Y)

R_2 = (ThetaT_XT_Y - n * np.mean(y) ** 2) / (YT_Y - n * np.mean(y) ** 2)
print('R_2 =', R_2)
F = (R_2 * (n - q - 1)) / ((1 - R_2) * q)
print('F =', F)

# проверка значимости
v_2_alpha = 4.74
if F > v_2_alpha:
    print('Уравнение регрессии значимо на уровне 0.05')

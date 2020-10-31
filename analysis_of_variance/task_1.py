# Однофакторный дисперсионный анализ
import numpy as np

I = 8
n = 56
alpha = 0.1
data = np.array([
    np.array([2.0, 2.8, 3.3, 3.2, 4.4, 3.6, 1.9, 3.3, 2.8, 1.1]),
    np.array([3.5, 2.8, 3.2, 3.5, 2.3, 2.4, 2.0, 1.6]),
    np.array([3.3, 3.6, 2.6, 3.1, 3.2, 3.3, 2.9, 3.4, 3.2, 3.2]),
    np.array([3.2, 3.3, 3.2, 2.9, 3.3, 2.5, 2.6, 2.8]),
    np.array([2.6, 2.6, 2.9, 2.0, 2.0, 2.1]),
    np.array([3.1, 2.9, 3.1, 2.5]),
    np.array([2.6, 2.2, 2.2, 2.5, 1.2, 1.2]),
    np.array([2.5, 2.4, 3.0, 1.5])
], dtype=object)
J = [10, 8, 10, 8, 6, 4, 6, 4]

mu_i = np.array([data[i].mean() for i in range(len(data))])
print('\nСредние:\n', mu_i)
mu = mu_i.mean()
print('\nОценка генерального среднего:', mu)
a_i = np.array([mu_i[i] - mu for i in range(len(mu_i))])
print('\nОценки дифференциальных эффектов:\n', a_i)
print('Проверка:', sum(a_i), '(что фактически равно нулю)\n')

SS_B = sum([J[i] * a_i[i] ** 2 for i in range(I)])
v_B = I - 1
MS_B = SS_B / v_B
print('SS_B =', SS_B, '\tv_B =', v_B, '\tMS_B =', MS_B)

SS_R = sum([(data[i][j] - mu_i[i]) ** 2 for i in range(I) for j in range(len(data[i]))])
v_R = n - I
MS_R = SS_R / v_R
print('SS_R =', SS_R, '\tv_R =', v_R, '\tMS_R =', MS_R)

# SS_T = SS_B + SS_R
SS_T = sum([(data[i][j] - mu) ** 2 for i in range(I) for j in range(len(data[i]))])
v_T = n - 1
print('SS_T =', SS_T, '\tv_T =', v_T)

F = MS_B / MS_R
print('\nF =', F)

F_alpha = 1.87
if F > F_alpha:
    print('Гипотеза отсутствия различия между средними весами в восьми приплодах отвергается!')

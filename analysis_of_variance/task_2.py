# Двухфакторный дисперсионный анализ
import numpy as np

I = 6
J = 9
data = np.array([
    np.array([5, 1, -4, 5, -13, -8, -2, -4, -10]),
    np.array([3, 6, -10, -2, -7, -2, -4, 2, 2]),
    np.array([8, 4, -14, -3, 3, 0, 5, -11, -12]),
    np.array([8, 10, -5, -1, 4, 2, 4, 1, -12]),
    np.array([4, -1, 7, -5, 5, -3, -7, -3, -6]),
    np.array([3, -9, 3, -8, -6, 0, -3, 8, -1]),
])

mu = data.mean()
print('Оценка генерального среднего mu =', mu)

<<<<<<< Updated upstream
y_i = [data[i].mean() for i in range(I)]
print('Средние по строкам:', y_i)
a_i = [y_i[i] - mu for i in range(I)]
print('a_i:', a_i)

y_j = [data.transpose()[j].mean() for j in range(J)]
print('Средние по столбцам:', y_j)
b_j = [y_j[j] - mu for j in range(J)]
=======
a_i = [data[i].mean() - mu for i in range(I)]
print('a_i:', a_i)

b_j = [data.transpose()[j].mean() - mu for j in range(J)]
>>>>>>> Stashed changes
print('b_j:', b_j, '\n')

SS_A = J * sum([a_i[i] ** 2 for i in range(I)])
v_A = I - 1
MS_A = SS_A / v_A
print('SS_A =', SS_A, '\tv_A =', v_A, '\tMS_A =', MS_A)

SS_B = I * sum([b_j[j] ** 2 for j in range(J)])
v_B = J - 1
MS_B = SS_B / v_B
print('SS_B =', SS_B, '\tv_B =', v_B, '\tMS_B =', MS_B)

<<<<<<< Updated upstream
SS_R = sum([(data[i][j] - y_i[i] - y_j[j] + mu) ** 2 for i in range(I) for j in range(J)])
=======
SS_R = sum([(data[i][j] - a_i[i] - b_j[j] + mu) ** 2 for i in range(I) for j in range(J)])
>>>>>>> Stashed changes
v_R = v_A * v_B
MS_R = SS_R / v_R
print('SS_R =', SS_R, '\tv_R =', v_R, '\tMS_R =', MS_R)

<<<<<<< Updated upstream
# SS_T = SS_A + SS_B + SS_R
=======
>>>>>>> Stashed changes
SS_T = sum([(data[i][j] - mu) ** 2 for i in range(I) for j in range(J)])
v_T = I * J - 1
print('SS_T =', SS_T, '\tv_T =', v_T)

<<<<<<< Updated upstream
F_A = MS_A / MS_R
F_B = MS_B / MS_R
v1_A = I - 1
v1_B = J - 1
v2 = v_R

print()
print('H_0: a_i = 0\t|\tH_0: b_j = 0')
print('F =', round(F_A, 6), '\t|\tF =', round(F_B, 6))
print('v1 =', v1_A, '\t\t\t|\tv1 =', v1_B)
print('v2 =', v2, '\t\t|\tv2 =', v2)
# v^2_0.05(5, 40) = 2.45
# v^2_0.05(8, 40) = 2.18
if F_A > 2.45:
    print('Гипотеза H_0: a_i = 0 отвергается')
else:
    print('Гипотеза H_0: a_i = 0 принимается')

if F_B > 2.18:
    print('Гипотеза H_0: b_j = 0 отвергается')
else:
    print('Гипотеза H_0: b_j = 0 принимается')
=======
print('Гипотеза a_i = 0')
F = MS_A / MS_R
v1 = I - 1
v2 = v_R
>>>>>>> Stashed changes

from math import fabs

resh = 1
a = -1
b = 1
x05 = []
result = []
N = int(input('Введите кол-во шагов: '))
h = (b-a)/N

for i in range(0, N):
    x05.append((a + i * h) - 0.5 * h)
    result.append(fabs(x05[i]) * h)

print('Интеграл равен: {}'.format(sum(result)))
difference = sum(result) - resh
print('Погрешность: {}%'.format(round(difference * 100)))

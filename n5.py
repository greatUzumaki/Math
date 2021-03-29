from math import pi, cos

resh = 0
a = pi / 4
b = (3 * pi) / 4
x1 = []
x2 = []
res1 = []
res2 = []
N = int(input('Введите кол-во шагов: '))
h = (b - a) / N

for i in range(0, N):
    x1.append(a + i * h)
    res1.append(cos(x1[i]))
    x2.append(x1[i] - h)
    res2.append(cos(x2[i]))

result = ((sum(res1) + sum(res2)) / 2) * h

print('Интеграл равен: {}'.format(result))
difference = result - resh
print('Погрешность: {}%'.format(round(difference * 100)))

from math import sin

resh = 2.10710945236653

a = 1.6
b = 2.4

x1 = []
x05 = []
x2 = []

res1 = []
res2 = []
res3 = []

N = int(input('Введите кол-вол шагов: '))
h = (b-a) / N

for i in range(0, N):
    x1.append(a + i * h)
    x05.append(x1[i] - 0.5*h)
    x2.append(x1[i] - h)

    res1.append((x1[i] + 1) * sin(x1[i]))
    res2.append((x05[i] + 1) * sin(x05[i]))
    res3.append((x2[i] + 1) * sin(x2[i]))


result = (sum(res3) + 4 * sum(res2) + sum(res1)) * h / 6

print('Интеграл равен: {}'.format(result))
difference = result - resh
print('Погрешность: {}%'.format(round(difference * 100)))



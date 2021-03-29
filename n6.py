resh = 0.410127340541491

a = 0.6
b = 1.4

x1 = []
x05 = []
x2 = []

res1 = []
res2 = []
res3 = []

N = int(input('Введите кол-вол шагов: '))
h = (b - a) / N

for i in range(0, N):
    x1.append(a + i * h)
    x05.append(x1[i] - 0.5 * h)
    x2.append(x1[i] - h)

    res1.append(1 / (x1[i] ** 2 + 1))
    res2.append(1 / (x05[i] ** 2 + 1))
    res3.append(1 / (x2[i] ** 2 + 1))

result = (sum(res3) + 4 * sum(res2) + sum(res1)) * h / 6

print('Интеграл равен: {}'.format(result))
difference = result - resh
print('Погрешность: {}%'.format(round(difference * 100)))

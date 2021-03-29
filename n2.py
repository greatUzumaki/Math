resh = 0.2471500840378944
a = 0.8
b = 1.8
x1 = []
x2 = []
res1 = []
res2 = []
N = int(input('Введите кол-во шагов: '))
h = (b - a) / N

for i in range(0, N):
    x1.append(a + i * h)
    res1.append(1/(2 * (x1[i]**2) + 1))
    x2.append(x1[i] - h)
    res2.append(1/(2 * (x2[i] ** 2) + 1))

result = ((sum(res1) + sum(res2)) / 2) * h

print('Интеграл равен: {}'.format(result))
difference = result - resh
print('Погрешность: {}%'.format(round(difference * 100)))

resh = 1/3
a = -1
b = 1
x05 = []
result = []
N = int(input('Введите кол-во шагов: '))
h = (b - a) / N

for i in range(0, N):
    x05.append((a + i * h) - 0.5 * h)
    result.append(x05[i] ** 2 / 2 * h)

print('Интеграл равен: {}'.format(sum(result)))
difference = sum(result) - resh
print('Погрешность: {}%'.format(round(difference * 100)))

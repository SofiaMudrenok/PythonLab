import random

b = int (input('b ='))
a = []
n = int (input('Введіть кількість рядків матриці:'))
m = int (input('Введіть кількість стовбців матриці:'))


for i in range(n):
    row = []
    for j in range(m):
        elem = random.randint(1,9)
        row.append(elem * b)
    a.append(row)

for i in range(len(a)):
    print(a[i])
import random
a = int (input('a ='))
b = []
n = int (input('Введіть кількість рядків матриці:'))
m = int (input('Введіть кількість стовбців матриці:'))
for i in range(n):
    row = []
    for j in range(m):
        elem = random.randint(1,9)
        row.append(elem*a)
        b.append(row)
for i in range(len(b)):
    print(b[i])

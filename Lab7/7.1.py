import random
res = 1
a = []
n = int (input('Введіть кількість рядків матриці:'))
m = int (input('Введіть кількість стовбців матриці:'))
for i in range(n):
    
        a.append([float(random.randint(-9,9))for j in range (m)])
for j in range(m):
    for i in range(n):
        if a[i][j]>0 and a[i][j]%2 == 0:
            res*=a[i][j]
print(a)
print(res)
import random
import array as np
a = []
n = int (input('Введіть кількість рядків матриці:'))
m = int (input('Введіть кількість стовбців матриці:'))
for i in range(n):
    
        a.append([float(random.randint(-9,9))for j in range (m)])
for j in range(m):
    if j%2 !=0:
        a[j].sort()
print(a)
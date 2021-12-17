import random
import array as np
b = []
count =0 
sum = 0
n=8
m=8
for i in range(n):
    
        b.append([float(random.randint(-9,9))for j in range (m)])
for j in range(m):
    for i in range(n):
        if b[i][j]<0:
            sum =sum + b[i][j]
print(b)
print(sum)
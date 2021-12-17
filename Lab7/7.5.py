import random
import array as np
b = []
count =0 
n=8
m=8
for i in range(n):
    
        b.append([float(random.randint(-9,9))for j in range (m)])
for j in range(m):
    for i in range(n):
        if b[i]==b[j]:
            count +=1
print(b)
print('Кількість = {0}'.format(m-count))
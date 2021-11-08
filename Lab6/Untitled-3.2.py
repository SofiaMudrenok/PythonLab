n = int(input('n= '))
a = [-4, 3]
new = []
sum = 0
b = int(input('b= '))
c = int(input('c= '))

for i in range(2, n+1):
    newA = a[i-1]**2 + 2 * a[i-2] - i
    a.append(newA)

for el in a:
    if b < el <= c:
        sum += el
        new.append(el)

avrg = sum / len(new)
print(avrg)

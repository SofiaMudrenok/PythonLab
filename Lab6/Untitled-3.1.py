n=int(input("Введіть розмірність масиву:"))
k = 0 
x=[]
for i in range (1,n+1):
     x.append (float(input('x[%i]= ' %i)))
for i in range (0,n-2):
    if (x[i]+x[i+2]==2*x[i+1]):
        print(' {0} {1} {2} '. format(x[i],x[i+1],x[i+2]))
        k=k+1
print('Кількість трійок {0}'.format(k))        
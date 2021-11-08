n=int(input("Введіть розмірність масиву:")) 
x=[]
for i in range (0,n):
     x.append (float(input('x[%i]= ' %i))) 
y=[]
for i in range (0,n):
     y.append (float(input('y[%i]= ' %i)))
s=0
for i in range(0,n):
    s=s+x[i]*y[i]
if s ==0:
    print("Вектори х , у   перпендикулярні")
else :
    print("Вектори х , у  не перпендикулярні")
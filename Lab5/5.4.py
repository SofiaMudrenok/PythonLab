x0 = 0 
x1 = 7 
n = int(input('n='))
xn=0
for i in range(1,n+1):
    xn=x1*(1+x0)
    x0=x1
    x1=xn
print ('x(n)={0}'.format(xn))

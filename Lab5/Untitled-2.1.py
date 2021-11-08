import math

n = int(input("n=")) 
x = float(input("x="))
a=1
sum = 0
for i in range (1,n+1 ):
    a=a*math.cos(x)
    sum = sum+a
print("sum{0}".format(sum))
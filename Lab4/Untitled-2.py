a= float(input("a="))
b= float(input("b="))
c= float(input("c="))
d= min(a,b) + (min(b,c))**2
if a>b:
   min = b
else :
   min = a
if b>c:
  min = c
else :
  min = b   
print(d)
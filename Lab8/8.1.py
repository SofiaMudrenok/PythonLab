x= int(input("x=")) 
y = int(input("y= "))
z = int(input("z= ")) 
def getmax ( a , b ):
    if a > b:
        max = a
    else:
        max = b
    return max

u = (getmax(x,z)+getmax(x+y,x*y))/getmax(x+y,x*y)**2
print(u)
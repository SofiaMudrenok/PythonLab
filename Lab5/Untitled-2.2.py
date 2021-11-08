a = int(input("a="))
b = int(input("b=")) 
n1 = 0
n2 = 0
a1=a
b1=b
while a//10 != 0:
    if (a%10 == 0):
         n1=n1+1
    a=a//10
while b//10 != 0:
    if (b%10 == 0):
        n2=n2+1
    b=b//10
if n1>n2 :
            print("Число {0} має більшу кількість нулів , ніж {1}". format(a1,b1))
else:
    if n2==n1 :
               print("Числа {0} і {1} мають рівну кількість нулів.". format(a1,b1))
    else : 
               print("Число {0} має більшу кількість нулів, ніж {1}.". format(b1,a1))

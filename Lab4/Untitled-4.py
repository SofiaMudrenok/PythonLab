x = float(input("Введіть x:"))
a = 2*x ** 2 -x -3
if a == 0:
       y=1
elif a > 0:
       y=2
elif a < 0:
       y=0
print("Результат={0}".format (y))
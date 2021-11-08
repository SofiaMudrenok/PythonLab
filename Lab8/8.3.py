def result(i):
    if i==0:
        return 0
    elif i==1 or i==2:
        return 9
    else:
        return result(i-1)+result(i-2)+result(i-3)

n=int(input("n"))
print("x{0}= {1}".format(n,result(n)))

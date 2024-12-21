n=int(input())
if n<1:
    print("Invalid Input")
else:
    if n>=40:
        n1=n//40
        for i in range(0,n1):
            print("XL",end="")
            n=n%40
    if n>=10:
        n2=n//10
        for i in range(0,n2):
            print("X",end="")
            n=n%10
    if n>=9:
        print("IX",end="")
        n-=9
    if n>=5:
        print("V",end="")
        n-=5
    if n>=4:
        print("IV",end="")
    for i in range(0,n):
        print("I",end="")
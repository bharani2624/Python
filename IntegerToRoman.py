n=int(input())
if n<=0 or n>=4000:
    print("Invalid Input")
else:
    th=n//1000
    for i in range(0,th):
        print("M",end="")
        n=n%1000
    if n>=900:
        print("CM",end="")
        n-=900
    elif n>=500:
        print("D",end="")
        n-=500
    elif n>=400:
        print("CD",end="")
        n-=400
    hundred=n//100
    for i in range(0,hundred):
        print("C",end="")
        n=n%100
    if n>=90:
        print("XC",end="")
        n-=90
    elif n>=50:
        print("L",end="")
        n-=50
    elif n>=40:
        print("XL",end="")
        n-=40
    ten=n//10
    for i in range(0,ten):
        print("X",end="")
        n=n%10
    if n>=9:
        print("IX",end="")
        n-=9
    elif n>=5:
        print("V",end="")
        n-=5
    elif n>=4:
        print("IV",end="")
        n-=4
    for i in range(0,n):
        print("I",end="")

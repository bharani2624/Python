sal=int(input())
g=input()
if sal<1:
    print("Invalid")
if 1<=sal<25000:
    print(5000)
elif 25000<sal<50000:
    print(7500)
elif 50000<sal:
    if g=='M':
        print(int(sal*0.1))
    else:
        print(int(sal*0.15))

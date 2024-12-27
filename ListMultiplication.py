def product(n):
    mul=1
    for i in range(0,len(n)):
        mul*=n[i]
    print(mul)
n=input()
n=n.split()
n=list(map(int,n))
product(n)
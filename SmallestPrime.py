def prime(start,n):
    if n==0 or n==1:
        return 0
    if start>n:
        return 0
    if start*start>n:
        return 1
    elif n%start==0:
        return 0
    return prime(start+1,n)

n=int(input())
count=5
n=n+1
while count!=0:
    if prime(2,n):
        print(n)
        count-=1
    n=n+1

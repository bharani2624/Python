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
ssum=0
for i in range(2,n):
    if n%i==0:
        if prime(2,i)==1:
            ssum+=i
print(ssum)


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
l=[]
for i in range(0,n):
    e=int(input())
    l.append(e)
for i in range(0,n):
    if prime(2,l[i])==0:
        print(l[i])
        break

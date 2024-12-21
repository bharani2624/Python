def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
n=int(input())
temp=n
ssum=0
while n!=0:
    rem=n%10
    ssum+=fact(rem)
    n=n//10
if ssum==temp:
    print(f'{temp} is a Strong Number')
else:
    print(f'{temp} is Not a Strong Number')

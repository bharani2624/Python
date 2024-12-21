n=int(input())
ssum=0
for i in range(1,n):
    if n%i==0:
        ssum=ssum+i
if ssum==n:
    print(f'{n} is an equal number')
else:
    print(f'{n} is not an equal number')
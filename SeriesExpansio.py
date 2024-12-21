n=float(input())
m=int(input())
t=float(1)
ssum=float(1)
for i in range(1,m):
    d=(2*i)*(2*i-1)
    t=-t * n * n /d
    ssum=ssum+t
print(f'{ssum:.2f}')
import math
n=int(input())
count=math.log10(n)+1
ssum=0
temp=n
while n!=0:
    rem=n%10
    ssum+=(pow(rem,int(count)))
    # print(ssum,end=" ")
    n=n//10
if ssum==temp:
    print(f'{temp} is a narcissistic number')
else:
    print(f'{temp} is not a narcissistic number')
# print(ssum)

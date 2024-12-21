n=int(input())
ssum=0
temp=n
while n!=0:
    rem=n%10
    ssum+=rem
    n=n//10
if temp%ssum==0:
    print(f'{temp} is Harshad number')
else:
    print(f'{temp} is Not Harshad number')
def happy(n):
    rem=0
    ssum=0
    while n!=0:
        rem=n%10
        ssum+=rem*rem
        n=n//10
    return ssum
n=int(input())
while n>9:
    n=happy(n)
if n==1:
    print(f'{n} is a Happy Number')
else:
    print(f'{n} is not a Happy Number')

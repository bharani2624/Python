def palindrome(n):
    rev=0
    temp=n
    rem=0
    while n!=0:
        rem=n%10
        rev=int(rev*10+rem)
        n=n//10
    if rev==temp:
        return 1
    else:
        return 0
n=int(input())
count=5
while count!=0:
    if palindrome(n)==1:
        print(n,end=" ")
        count-=1
        n+=1
    n+=1
n=int(input())
product=1
while n!=0:
    rem=n%10
    product*=rem
    n=n//10
if product==0:
    print("Invalid Input")
else:
    print(product)
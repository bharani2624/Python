n=int(input())
if n<1:
    print("Invalid Input")
else:
    temp=n
    while(n%2==0):
        n=n//2
    while(n%3==0):
        n=n//3
    while(n%5==0):
        n=n//5
    if n==1:
        print(f'{temp} is a Ugly Number')
    else:
        print(f'{temp} is not a Ugly Number')
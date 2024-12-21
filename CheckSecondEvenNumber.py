n=int(input())
m=int(input())
if n%2!=0 or m%2!=0:
    print("Invalid")
else:
    while n<=m:
        n+=1
        if n%2==0:
            print(n)
            break
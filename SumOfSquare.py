n=int(input())
if n<0:
    print("Invalid")
else:
    ssum=0
    for i in range(0,n+1):
        ssum+=pow(i,2)
    print(int(ssum))
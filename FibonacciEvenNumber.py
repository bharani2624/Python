n=int(input())
if n<1:
    print("Invalid")
else:
    n1=0
    n2=1
    ssum=0
    while ssum<=n:
        if ssum%2==0:
            print(ssum,end=" ")
        ssum=n1+n2
        n1=n2
        n2=ssum
 
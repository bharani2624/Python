n=int(input())
if n<1:
    print("Invalid Input")
else:
    count=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(count,end=" ")
            count+=1
        for k in range(count-2,count-i-1,-1):
            print(k,end=" ")
        print("",end="\n")

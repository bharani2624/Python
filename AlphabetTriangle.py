n=int(input())
if n<1:
    print("Invalid")
else:
    count=65
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(chr(count),end=" ")
            count+=1
        print("",end="\n")
        
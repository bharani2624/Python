n=int(input())
if n<1:
    print("Invalid")
else:
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end=" ")
        print("",end="\n")
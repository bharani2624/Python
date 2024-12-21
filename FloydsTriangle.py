n=int(input())
if n<1:
    print(f'{n} is Invalid input')
else:
    count=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(count,end=" ")
            count+=1
        print("",end="\n")

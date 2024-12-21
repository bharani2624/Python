n=int(input())
if n<1:
    print("Invalid")
else:
    ssum=0
    for i in range(0,n):
        ssum+=1/pow(2,i)
    print(f'{ssum:.2f}')
n=int(input())
if n<1:
    print("Invalid")
else:
    ssum=0
    for i in range(1,n+1):
        ssum+=(1/i)
    print(f'{ssum:.2f}')
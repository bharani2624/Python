n=int(input())
if n<0:
    print("Invalid Input")
elif n==1:
    print(0)
else:    
    n1=0
    n2=1
    fibonacciSum=0
    print(f'{n1},{n2},',end="")
    for i in range(2,n):
        fibonacciSum=n1+n2
        n1=n2
        n2=fibonacciSum
        print(f'{fibonacciSum},',end="")
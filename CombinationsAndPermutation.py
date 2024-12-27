def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
def result(n,r):
    ncr=factorial(n)//(factorial(r)*factorial(n-r))
    print(ncr)
result(int(input()),int(input()))
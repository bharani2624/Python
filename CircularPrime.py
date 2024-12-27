def prime(n,i=2):
    if n==0 or n==1:
        return False
    if n==2 or n==3:
        return True
    if i*i>n:
        return True
    elif n%i==0:    
        return False
    return prime(n,i+1)
def rotate(n,length):
    temp=n//pow(10,length-1)
    rem=n%10
    n=rem*(pow(10,length-1))+temp
    return n
n=int(input())
length=len(str(n))
for i in range(0,length):
    n=rotate(n,length)
    if prime(n):
        continue
    else:
        print("Not A Circular Prime")
        exit()
print("Circular Prime")
import math
n=int(input())
count=int(math.log10(n)+1)
square=int(n*n)
last=square%int(pow(10,count))
print(last)
if last==n:
    print(f'{n} is an Automorphic Number.')
else:
    print(f'{n} is not an Automorphic Number.')

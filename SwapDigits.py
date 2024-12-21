import math
n=int(input())
count=int(math.log10(n)+1)
last=(n%10)*pow(10,count-2)
n=n//10
first=int(n)//int(pow(10,count-2))
n=n%int(pow(10,count-2))
print(((last+n)*10)+first)
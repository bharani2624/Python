n=int(input())
m=int(input())
l=[]
for i in range(0,n):
    element=input()
    l.append(element)

for i in range(m):
    first=l[0]
    for j in range(0,n-1):
        l[j]=l[j+1]
    l[n-1]=first
print(l)

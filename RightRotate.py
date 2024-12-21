n=int(input())
m=int(input())
l=[]
for i in range(0,n):
    elements=input()
    l.append(elements)
l=l[-m:]+l[:-m]
print(l)
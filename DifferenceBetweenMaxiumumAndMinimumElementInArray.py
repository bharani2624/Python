n=int(input())
l=[]
for i in range(0,n):
    element=int(input())
    l.append(element)
l.sort()
print(l[n-1]-l[0])

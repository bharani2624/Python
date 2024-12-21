n=int(input())
l=[]
for i in range(0,n):
    element=int(input())
    l.append(element)
for i in range(0,n):
    print(l[i]*l[i],end=" ")

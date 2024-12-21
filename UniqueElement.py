n=int(input())
l=[]
for i in range(0,n):
    e=int(input())
    l.append(e)
l.sort()
printed=[0]*n
for i in range(0,n):
    if printed[i]!=1:
        for j in range(i+1,n):
            if l[i]==l[j]:
                printed[j]=1
                printed[i]=1
for i in range(0,n):
    if printed[i]!=1:
        print(l[i])
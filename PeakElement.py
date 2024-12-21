n=int(input())
l=[]
for i in range(0,n):
    e=int(input())
    l.append(e)
ssum=0
if l[0]>l[1]:
    ssum=l[0]+l[1]
    l[0]=ssum
    # print(ssum)
elif l[n-1]>l[n-2]:
    ssum=l[n-1]+l[n-2]
    l[n-1]=ssum
    # print(ssum)
else:
    for i in range(1,n-1):
        if l[i]>l[i-1] and l[i]>l[i+1]:
            l[i]=l[i-1]+l[i]+l[i+1]
            # print(l[i]+l[i-1]+l[i+1])
            break
print(l)
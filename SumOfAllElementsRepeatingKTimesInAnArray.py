n=int(input())
k=int(input())
l=[]
for i in range(0,n):
    element=int(input())
    l.append(element)
l.sort()
ssum=0
count=1
dl=[]
for i in range(0,n-1):
    if l[i]==l[i+1]:
        count+=1
    else:    
        if k==count:
            dl.append(l[i])        
        count=1
if count==k:
    dl.append(l[-1])
dl=list(set(dl))
print(sum(dl))
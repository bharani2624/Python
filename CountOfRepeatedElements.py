n=int(input())
l=[]
count=0
for i in range(0,n):
    e=int(input())
    l.append(e)
l.sort()
for i in range(0,n-1):
    if l[i]==l[i+1]:
        count+=1
print(count)
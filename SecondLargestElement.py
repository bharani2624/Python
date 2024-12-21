n=int(input())
l=[]
for i in range(0,n):
    e=int(input())
    l.append(e)
l.sort()
print(l[-2])
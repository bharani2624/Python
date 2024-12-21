n=int(input())
l=[]
for i in range(0,n):
    e=int(input())
    l.append(e)
l.sort()
for i in l:
    if i%2==0:
        print(i)
for i in l:
    if i%2!=0:
        print(i)
n=int(input())
l=[]
unique=[]
duplicate=[]
for i in range(0,n):
    element=int(input())
    l.append(element)
for i in l:
    if i not in unique:
        unique.append(i)
    elif i not in duplicate:
        duplicate.append(i)
ssum=sum(duplicate)
print(duplicate)
print(ssum)
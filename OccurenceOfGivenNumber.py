l=[]
n=int(input())
# m=int(input())
for i in range(0,n):
    elements=int(input())
    l.append(elements)
t=tuple(l)
count=0
sl=list(set(l))
for i in range(0,len(sl)):
    occurence=t.count(sl[i])
    print(f'{sl[i]}={occurence}',end="\n")

# occurence=t.count(m)
# print(occurence)

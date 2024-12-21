n=int(input())
m=int(input())
l=[]
for i in range(0,n):
    element=int(input())
    l.append(element)
if m in l:
    l.remove(m)
    print(l)
else:
    print("Element Not Found")
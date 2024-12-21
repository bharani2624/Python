n=int(input())
l=[]
for i in range(0,n):
    e=input()
    l.append(e)
dl=[]
for i in range(0,n):
    dl.append(l[i])
    s=str(l[i])
    s=s.lower()
    ls=list(s)
    ls.sort()
    s=''.join(ls)
    l[i]=s
printed=[0]*n
for i in range(0,n):
    if printed[i]!=1:
        print(dl[i],end=" ")
        printed[i]=1
        for j in range(i+1,n):
            if l[i]==l[j]:
                print(dl[j],end="\n")
                printed[j]=1
        


def inp():
    n=int(input())
    m=int(input())
    o=int(input())
    p=int(input())
    l=[]
    li=[]
    for i in range(n):
        row=list(map(int,input().split()))
        l.append(row)
    for i in range(o):
        row=list(map(int,input().split()))
        li.append(row)
    result(l,li,n,m,o,p)

def result(l,li,n,m,o,p):
    res=[[0 for _ in range(p)] for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                res[i][j]+=l[i][k]*li[k][j]
    for row in res:
       print(" ".join(map(str,row)))
inp()
def result(n):
    l=[]
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            l.append(n[i]*n[j])
    # print(l)
    Max=0
    for num in l:
        Max=max(Max,digitSum(num))
    print(Max)
def digitSum(n):
    res=0
    for i in range(len(str(n))):
        rem=n%10
        n//=10
        res+=rem
    return res
n=list(map(int,input().split()))
result(n)


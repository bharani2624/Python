n=int(input())
m=int(input())
seriesSum=0
ssum=0
for i in range(0,m):
    seriesSum=seriesSum*10+n
    ssum+=seriesSum
    if i<m-1:
        print(seriesSum,end="+")
    else:
        print(seriesSum,end="")
print(f'\n{ssum}')
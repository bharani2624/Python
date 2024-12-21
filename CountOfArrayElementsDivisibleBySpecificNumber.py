n=int(input())
m=int(input())
l=[]
count=0
for i in range(0,n):
    e=int(input())
    l.append(e)
for i in l:
    if i%m==0:
        count+=1
if count>0:
    print(count)
else:
    print(f"None Of The Elements Are Divisible By {m}")

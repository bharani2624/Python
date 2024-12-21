p=int(input())
q=int(input())
t=p*q
if t%2==0:
    d=(t*0.1)
else:
    d=(t*0.15)
print(t-d)
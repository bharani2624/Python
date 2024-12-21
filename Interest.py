p=int(input())
r=float(input())
t=float(input())
year=t*12
compound=pow((1+r/100/12),year)
a=p*(compound)
print(format(a,".2f"))

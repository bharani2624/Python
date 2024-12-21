a=int(input())
if a<0:
    print("Invalid amount")
elif a==0:
    print("No cash needed")
else:
    n1=0
    n2=0
    n3=0
    n4=0
    n5=0
    n=0
    if(a>=500):
        n1=a//500
        a=a%500
    elif a>=100:
        n2=a//100
        a=a%100
    elif a>=50:
        n3=a//50
        a=a%50
    elif a>=20:
        n4=a//20
        a=a%20
    elif a>=10:
        n5=a//10
        a=a%10
    else:
        n=a
    print(f'{n1},{n2},{n3},{n4},{n5},{n}')
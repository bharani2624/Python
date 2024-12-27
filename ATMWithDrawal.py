def atm(w,b):
    denominations=[10,20,50,100,500,1000,2000]
    if w>b:
        print(w)
        print("Not Possible")
    if not any(w%denom==0 for denom in denominations):
        print(f'Not possible and balance:{w-b}')
    else:
        print("possible")
amount=input().split()
amount=list(map(int,amount))
print(amount)
balance=int(input())
for amo in amount:
    atm(amo,balance)
 

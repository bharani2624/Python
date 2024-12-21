c=int(input())
s=int(input())
if c<0 or s<0:
    print("Invalid")
else:    
    p=s-c
    if p>0:
        print("Profit")
    elif p==0:
        print("Break-even")
    else:
        print("Loss")
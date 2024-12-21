import math
n=int(input())
if 1<=n<=50:
    if n%3==0 and n%5==0:
        print("Occupied")
    else:
        print("Not Booked")

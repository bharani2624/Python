e=int(input())
if e<=0:
    print("Invalid")

else:
    if e<=50:
        bill=e*0.5
    elif 51<=e<=150:
        bill=50 * 0.5 + (e-50) * 0.75
    elif 151<=e<=250:
        bill=50 * 0.5 + 100 * 0.75 + (e-150) * 1.20
    else:
        bill=50 * 0.5 + 100 * 0.75 + 100 * 1.20 + (e-250)*1.50
s=bill*0.2
print(f'{bill+s:.2f}')
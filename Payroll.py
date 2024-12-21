sal=int(input())
if sal<=0:
    print("Invalid Salary")
else:
    if sal<=10000:
        hra=(sal*0.2)
        da=(sal*0.8)
        t=(sal+hra+da)
        print(f'{t:.2f}')
        # print(float(sal+hra+da))
    elif 10000<sal<=20000:
        hra=(sal*0.25)
        da=(sal*0.9)
        t=(sal+hra+da)
        print(f'{t:.2f}')
        # print(float(sal+hra+da))
    else:
        hra=(sal*0.3)
        da=(sal*0.95)
        t=(sal+hra+da)
        print(f'{t:.2f}')   

def decimal_to_binary(n):
    integer=int(n)
    decimal=float(n-integer)
    # print(n,integer)
    binInteger=format(integer,"07b")
    res=""
    res+=binInteger+"."
    for i in range(3):
        whole,decimal=str((decimal_converter(decimal))*2).split(".")
        decimal=int(decimal)
        res+=whole
    print(res)
def decimal_converter(num):
    while num>=1:
        num/=10
    return num
decimal_to_binary(float(input()))

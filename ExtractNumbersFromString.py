s=input()
st=s.split(" ")
for i in range(0,len(st)):
    s=str(st[i])
    if s.isnumeric():
        print(s)
# print(st)
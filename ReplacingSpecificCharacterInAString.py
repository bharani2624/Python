s=input()
rc1='e'
rc2='h'
rc3='n'
s=s.replace(rc1,'f')
s=s.replace(rc2,'j')
for i in s:
    if i.isdigit():
        s=s.replace(i,rc3)
print(s)

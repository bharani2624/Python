s=input()
s=s.lower()
s=s.replace(" ","")
l=list(s)
l.sort()
s=''.join(l)
ma=0
count=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        if ma<count:
            ma=count
            mindex=i-count+1
        count=1
if ma<count:
    ma=count+1
    mindex=len(s)-1-count
print(s[mindex])
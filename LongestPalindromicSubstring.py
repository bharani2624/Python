s=input()
st=[]
for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        l=[]
        for k in range(i,j+1):
            l.append(s[k])
        st.append(l)
ma=0
sl=[]
for i in range(0,len(st)):
    l=len(st[i])
    ss=''.join(st[i])
    sl.append(ss)
    if ma<l:
        ma=l
        mindex=i
string=''.join(st[mindex])
maximum=0
maxindex=0
for i in range(0,len(sl)):
    s=''.join(sl[i])
    string=s[::-1]
    if s==string:
        if maximum<len(s):
            maximum=len(s)
            maxindex=i
    s=""
    string=""
print(sl[maxindex])

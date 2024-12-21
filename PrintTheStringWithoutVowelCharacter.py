s=input()
st=s.lower()
for i in range(0,len(s)):
    if st[i]=='a' or st[i]=='e' or st[i]=='i' or st[i]=='o' or st[i]=='u':
        continue
    else:
        print(s[i],end="")

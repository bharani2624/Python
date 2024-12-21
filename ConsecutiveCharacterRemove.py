s=input()
string=""
for i in range(0,len(s)):
    if s[i]==s[i-1]:
        continue
    else:
        string+=s[i]
if s==string:
    print(f'{s} has no duplicate characters')
else:
    print(string)
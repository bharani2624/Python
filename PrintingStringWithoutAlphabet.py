s=input()
for string in s:
    if string.isalpha():
        continue
    else:
        print(string,end="")
def count(s):
    cap=0
    small=0
    for i in range(len(s)):
        if s[i].islower():
            small+=1
        if s[i].isupper():
            cap+=1
    print(f'{cap} {small}')
count(input())
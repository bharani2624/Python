def key(words):
    l1="qwertyuiop"
    l2="asdfghjkl"
    l3="zxcvbnm"
    res=[]
    for word in words:
        temp=word
        word=word.lower()
        if len(set(l1+word))==len(l1) or len(set(l2+word))==len(l2) or len(set(l3+word))==len(l3):
            res.append(temp)
    print(res)
key(input().split())
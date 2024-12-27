def product(words):
    words=words.split()
    masked=[]
    for word in words:
        mask=0
        for char in word:
            mask|=1<<(ord(char)-ord('a'))
        masked.append(mask)
    max_product=0
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if masked[i] & masked[j]==0:
                product=len(words[i])*len(words[j])
                max_product=max(max_product,product)
    print(max_product)
product(input())

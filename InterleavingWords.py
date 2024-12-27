def printList(list):
    return "".join(list)

def printIlsRecur(str1, str2, l, n, m, i):
    if m == 0 and n == 0:
        print(printList(l))
    if n != 0:
        l[i] = str1[0]
        printIlsRecur(str1[1:], str2, l, n-1, m, i + 1)
    if m != 0:
        l[i] = str2[0]
        printIlsRecur(str1, str2[1:], l, n, m-1, i + 1)
str1 = input()
str2 = input()
iStr = [''] * (len(str1)+len(str2))
printIlsRecur(str1, str2, iStr,len(str1), len(str2),0)
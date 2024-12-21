a=input()
if a.isalpha():
    # print("Alphabet")
    a=a.lower()
    if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
        print("Vowel")
    else:
        print("Consonant")
elif a.isdigit():
    print("Number")
else:
    print("Special Characters")
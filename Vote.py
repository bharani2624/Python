name=input()
age=int(input())
gender=int(input())
if age<18:
    print("Not Eligible")
else:
    if gender==1:
        print(f'Eligible Status:Eligible')
        print(f'Salutation:"Mr.{name}"')
    elif gender==2:
        print(f'Eligible Status:Eligible')
        print(f'Salutation:"Ms.Emma"')
    else:
        print(f'Invalid')
time=int(input())
hour=time//100
minutes=time%100

if hour==0 or hour==24:
    h12=12
    period="AM"
elif hour==12:
    h12=12
    period="PM"
elif hour>12:
    h12=hour-12
    period="PM"
else:
    h12=hour
    period="AM"
print(f'{h12}:{minutes:02} {period}')
a=[]
for i in range(0,5):
    marks=int(input())
    a.append(marks)
sum=0
for i in range(0,5):
    sum+=a[i]
avg=float(float(sum)/float(5))
# print(format(avg,".2f"))
print(f'{avg:.2f}')
# print(float(float(sum)/float(5)))
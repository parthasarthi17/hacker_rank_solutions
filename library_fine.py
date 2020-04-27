d1,m1,y1=map(int,input().split()) #returning date
d2,m2,y2=map(int,input().split()) #book to be returned so tht fine is not paid
fine=0
if d1>d2 and m1==m2 and y1==y2:
    fine=(d1-d2)*15
elif m1>m2 and y1==y2:
    fine=(m1-m2)*500
elif y1>y2:
    fine=(y1-y2)*10000
print(fine)
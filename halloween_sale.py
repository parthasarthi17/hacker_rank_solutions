p,d,m,s=map(int,input().split())#first price,after_first,minimum_price,price
count=0
k=1
while s>0 :
    if count==0:
        s=s-p
        count+=1
        continue
    a=d*k
    if p-a<=m:
        a=m
    s=s-p+(a)
    count+=1
    k+=1
print(count)
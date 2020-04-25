def rev(n):
    reverse=0
    while n>0:
        remainder=n%10
        reverse=reverse*10+remainder
        n=n//10
    return reverse
    
start_date,end_date,k=map(int,input().split())


li=[]
for w in range(start_date,end_date+1):
    li.append(w)
count=0
for x in li:
    a=x-rev(x)
    if a<0:
        a=a*(-1)
    if a%k==0:
        count=count+1
print(count)
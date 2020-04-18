n=list(map(int,input().split())) #entering n ,m
a=list(map(int,input().split()))
b=list(map(int,input().split()))
i=1
num=0
for w in a:
    if b[i]%w==0:
        num=num+1
print(num)
num1=num
for w in b:
    if w%a[i]==0:
        num1=num1+1
print(num1-num)
    

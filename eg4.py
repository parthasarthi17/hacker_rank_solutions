def how(num):
    num=num-1
    a=((2+(num-1))*num)/2
    return int(a)    
a=[1,2,3,4,5]

p=len(a)
num=0
b=0n
for i in range(how(p)):
    while b<len(a):
        print(a[i+1],"++",a[b])
        if (a[i+1]+a[b])%3==0:
            num=num+1
        b=b+1
    a.pop(0)
    b=1
print(num)
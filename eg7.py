def how(num):
    num=num-1
    a=((2+(num-1))*num)/2
    return int(a)-1    
a=[1,2,3,4,5]
b=how(len(a))
k,j=0,1
for i in range(1,b):
    while i<len(a):
        print(a[k],a[j])
        j=j+1
        if j==len(a):
            j=0
            k=k+1
        if k==len(a)-1:
            break
    i=i+1
    
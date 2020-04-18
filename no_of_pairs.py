n=int(input())
li=list(map(int,input().split()))
a=len(li)
i=0
j=1
while i<a:
    while j<a:
        if li[j]==li[i]:
            #print("j=",j,"i=",i)
            li.pop(i)
            #print("li",li)
            li.pop(j-1)
            j=0
        j=j+1
        a=len(li)
    i=i+1
    a=len(li)
#print(li)
print((n-len(li))/2)

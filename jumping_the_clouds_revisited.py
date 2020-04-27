n,k=map(int,input().split())#no of clouds , length of jump
c=list(map(int,input().split()))
e=100
index=0
print(k)
i=0
while e>0:
    print("upr",k+index)
    if (k*i)+index>=len(c):
        print("yhn")
        index=index-len(c)
        i=0
    print("Chahoye",c[(k*i)+index])
    if c[(k*i)+index]==1:
       e=e-3 
    elif c[(k*i)+index]==0:
        e-=1
    
    index+=k
   
    print(index)
    if index==0:
        break
    i+=1
    print("e",e)

n,d=map(int,input().split())
arr=list(map(int,input().split()))
w=0
i=0
li=[]
mini=[]
k=arr[0]
n=0
for m in range(1,len(arr)-1): 
    while w<len(arr):
       if arr[w]-k==d:
           if n==0:
               mini.append(k)
               n+=1
           mini.append(arr[w])
           k=arr[w]
           n+=1
       if n==3:
            n=0
            break
            
       w+=1
    if len(mini)==3:
        li.append(mini)
    mini=[]
    k=arr[m]
    w=m
print(len(li))

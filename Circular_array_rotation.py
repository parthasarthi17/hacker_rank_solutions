n,k,q=map(int,input().split()) #no_of_elements,rotation_count,no of queries
a=list(map(int,input().split()))
li=[]
for i in range(q):
    x=int(input())
    li.append(x)
front=0
rear=len(a)-1
#print(front,rear)
for w in a:
    while k>0:
        if front==len(a):
           front=0
        if rear==len(a)-1:
            rear=0
        
        a[front]=a[front]
        a[rear+1]=a[rear]
        k-=1
        front+=1
        rear+=1
print(a)
        
